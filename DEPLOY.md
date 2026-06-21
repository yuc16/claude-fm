# 部署手册：把播客托管到自有服务器，供小宇宙 RSS 订阅

目标：东京 Ubuntu 服务器用 Caddy 托管音频 + `feed.xml`，对外 `https://fm.yccode.xyz`，
小宇宙按 RSS 地址订阅，448 集自动出现。

占位符：`<IP>` = 服务器公网 IP；`<user>` = SSH 登录名（腾讯云轻量常见 `ubuntu` 或 `lighthouse`）。

---

## 第 1 步　拿服务器公网 IP

腾讯云控制台实例列表的「公网 IP」，或 SSH 到服务器后 `curl ifconfig.me`。记下 `<IP>`。

## 第 2 步　Cloudflare 加解析

[dash.cloudflare.com](https://dash.cloudflare.com) → 域名 **yccode.xyz** → **DNS → Records → Add record**：

- Type：`A`
- Name：`fm`
- IPv4 address：`<IP>`
- **Proxy status：DNS only（灰色云，务必点掉橙色）**
- Save

验证（Mac）：`dig +short fm.yccode.xyz` 回显 `<IP>` 即生效（等 1–3 分钟）。

## 第 3 步　放行端口 80、443

- 腾讯云控制台 → 该实例 **防火墙/安全组** → 添加入站：TCP **80**、TCP **443**，来源 `0.0.0.0/0`
- 服务器上若启用了 ufw：`sudo ufw allow 80 && sudo ufw allow 443`

## 第 4 步　装 Caddy 并配置（SSH 在服务器上执行）

```bash
# 安装 Caddy
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install -y caddy

# 建目录（放音频和 feed）
sudo mkdir -p /srv/claudefm/audio/{engineering,research,news,blog}
sudo chown -R $USER:$USER /srv/claudefm

# 写 Caddy 配置（自动 HTTPS）
sudo tee /etc/caddy/Caddyfile >/dev/null <<'EOF'
fm.yccode.xyz {
    root * /srv/claudefm
    file_server
    encode gzip
}
EOF
sudo systemctl restart caddy
```

## 第 5 步　验证 HTTPS

```bash
# 服务器上放个测试文件
echo ok | sudo tee /srv/claudefm/test.txt
# Mac 上访问
curl -I https://fm.yccode.xyz/test.txt      # 出 HTTP/2 200 即成功
```

不通的常见原因：域名没解析生效（等几分钟）、安全组没放行、Caddy 还在签证书（再等一分钟）。

## 第 6 步　把音频和 feed 传上去（Mac 上，项目目录里执行）

```bash
cd /Users/wangyc/Desktop/projects/claude-fm

# 先在本地生成最新 feed
uv run claude-fm feed

# 传四个源的音频（约 3.2GB，按上行带宽耗时）
rsync -avz --progress "content/anthropic/engineering/audio/" <user>@<IP>:/srv/claudefm/audio/engineering/
rsync -avz --progress "content/anthropic/research/audio/"    <user>@<IP>:/srv/claudefm/audio/research/
rsync -avz --progress "content/anthropic/news/audio/"        <user>@<IP>:/srv/claudefm/audio/news/
rsync -avz --progress "content/claude/blog/audio/"           <user>@<IP>:/srv/claudefm/audio/blog/

# 传 feed
rsync -avz "content/feed.xml" <user>@<IP>:/srv/claudefm/feed.xml
```

## 第 7 步　封面图

做一张 **≥1400×1400 的 jpg**（不要用 Anthropic/Claude 官方 logo），传上去：

```bash
rsync -avz 你的封面.jpg <user>@<IP>:/srv/claudefm/cover.jpg
```

## 第 8 步　验证 feed 并加进小宇宙

```bash
curl -I https://fm.yccode.xyz/feed.xml       # 200
```

打开**小宇宙 App →「发现」→ 顶部搜索框 / 添加播客**，粘贴：

```
https://fm.yccode.xyz/feed.xml
```

448 集会全部出现，开听 🎉

---

## 以后每周更新（周日）

```bash
cd /Users/wangyc/Desktop/projects/claude-fm
uv run claude-fm weekly      # 三源增量解读 + news 上周周报
uv run claude-fm feed        # 重新生成 feed.xml

# 只传新增音频（rsync 自动跳过已存在的）+ 刷新 feed
rsync -avz --progress "content/anthropic/engineering/audio/" <user>@<IP>:/srv/claudefm/audio/engineering/
rsync -avz --progress "content/anthropic/research/audio/"    <user>@<IP>:/srv/claudefm/audio/research/
rsync -avz --progress "content/anthropic/news/audio/"        <user>@<IP>:/srv/claudefm/audio/news/
rsync -avz --progress "content/claude/blog/audio/"           <user>@<IP>:/srv/claudefm/audio/blog/
rsync -avz "content/feed.xml" <user>@<IP>:/srv/claudefm/feed.xml
```

小宇宙会自动拉到新增的集。
