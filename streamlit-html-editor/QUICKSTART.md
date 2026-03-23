# 🚀 快速部署指南

## 方式 1: 本地运行（最快）

```bash
# 1. 解压文件
tar -xzf streamlit-html-editor.tar.gz
cd streamlit-html-editor

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行应用
streamlit run app.py
```

应用会在浏览器自动打开：`http://localhost:8501`

---

## 方式 2: 部署到 Streamlit Cloud（永久在线）

### 步骤 1: 上传到 GitHub

```bash
# 1. 在 GitHub 创建新仓库（例如：html-editor）

# 2. 进入项目文件夹
cd streamlit-html-editor

# 3. 初始化 Git 并推送
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/html-editor.git
git push -u origin main
```

### 步骤 2: 部署到 Streamlit Cloud

1. 访问 https://share.streamlit.io
2. 使用 GitHub 登录
3. 点击 **"New app"**
4. 选择你的仓库：`你的用户名/html-editor`
5. Branch: `main`
6. Main file: `app.py`
7. 点击 **"Deploy"**

⏰ 等待 2-3 分钟，你的应用就上线了！

---

## 🎯 部署后你会得到：

- ✅ 一个永久的在线地址（例如：`your-app.streamlit.app`）
- ✅ 自动 HTTPS 加密
- ✅ 免费托管（Streamlit 社区版）
- ✅ 自动更新（每次 push 代码后自动部署）

---

## ⚡ 一键命令（如果你有 Git 和 Streamlit CLI）

```bash
# 解压并进入目录
tar -xzf streamlit-html-editor.tar.gz && cd streamlit-html-editor

# 安装并运行
pip install -r requirements.txt && streamlit run app.py
```

---

## 💡 提示

- 第一次部署建议使用本地运行测试
- Streamlit Cloud 免费版限制：1GB RAM, 1 CPU
- 更多配置选项请查看 README.md

**祝部署顺利！🎉**
