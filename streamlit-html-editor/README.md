# HTML 可视化编辑器 - Streamlit 部署包

一个可以在线编辑 HTML 文件的可视化编辑器，支持文字编辑和图片替换。

## 功能特性

✅ **可视化编辑** - 直接点击文字即可修改内容  
✅ **图片管理** - 点击图片上传新图或修改 URL  
✅ **外链支持** - 完整支持外链图片的编辑  
✅ **一键导出** - 导出修改后的 HTML 文件  
✅ **Base64 嵌入** - 上传的图片自动转换为 Base64 格式  

---

## 📦 文件结构

```
html-editor/
├── app.py                          # Streamlit 主应用
├── html_editor_standalone.html     # HTML 编辑器（独立版本）
├── requirements.txt                # Python 依赖
└── README.md                       # 说明文档
```

---

## 🚀 本地运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
streamlit run app.py
```

应用会自动在浏览器中打开 `http://localhost:8501`

---

## ☁️ 部署到 Streamlit Cloud

### 方法 1：通过 GitHub（推荐）

1. **创建 GitHub 仓库**
   - 登录 GitHub，创建新仓库（例如：`html-editor`）
   - 将所有文件上传到仓库

2. **连接 Streamlit Cloud**
   - 访问 [share.streamlit.io](https://share.streamlit.io)
   - 使用 GitHub 账号登录
   - 点击 "New app"

3. **配置部署**
   - Repository: 选择你的 `html-editor` 仓库
   - Branch: `main`
   - Main file path: `app.py`
   - 点击 "Deploy"

4. **等待部署**
   - 几分钟后，你的应用就会上线
   - 获得一个公开的 URL（例如：`your-app.streamlit.app`）

### 方法 2：直接从本地部署

1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 点击 "New app" → "I have an app"
3. 选择 "Paste GitHub URL" 并输入你的仓库地址
4. 或者使用 Streamlit CLI：
   ```bash
   streamlit cloud deploy app.py
   ```

---

## 📖 使用说明

### 上传 HTML 文件
1. 点击"选择文件"按钮
2. 选择你要编辑的 `.html` 文件
3. 文件内容会显示在编辑区

### 编辑文字内容
- 直接点击任何文字
- 像在 Word 里一样编辑
- 修改会自动保存

### 编辑图片
1. **点击图片** - 会打开图片编辑面板
2. **修改 URL** - 在输入框中修改图片链接
3. **上传新图** - 点击"上传新图片"选择本地文件
4. **确认修改** - 点击"确认修改"应用更改

### 导出文件
- 编辑完成后，点击"导出 HTML"按钮
- 修改后的 HTML 文件会自动下载到本地

---

## 🛠️ 技术栈

- **前端**: React 18 + Tailwind CSS
- **后端**: Streamlit (Python)
- **部署**: Streamlit Cloud

---

## 💡 注意事项

1. **图片处理**
   - 上传的本地图片会转换为 Base64 格式嵌入 HTML
   - 外链图片保持 URL 形式
   - Base64 嵌入的优点：不依赖外部图片链接，HTML 文件独立可用

2. **浏览器兼容性**
   - 推荐使用 Chrome、Firefox、Edge 等现代浏览器
   - Safari 可能存在部分样式差异

3. **文件大小**
   - 建议 HTML 文件 < 10MB
   - Base64 图片会增大文件体积（约为原图的 1.33 倍）

---

## 🔧 自定义配置

### 修改编辑器高度

编辑 `app.py` 第 23 行：

```python
components.html(html_content, height=1000, scrolling=True)
#                                    ↑
#                          修改这个数值（像素）
```

### 修改页面标题

编辑 `app.py` 第 5-9 行：

```python
st.set_page_config(
    page_title="HTML 可视化编辑器",  # 修改这里
    page_icon="✏️",                  # 修改图标
    layout="wide",
    initial_sidebar_state="collapsed"
)
```

---

## 📝 更新日志

**v1.0.0** (2024)
- ✅ 初始版本发布
- ✅ 支持 HTML 文件上传和编辑
- ✅ 支持图片 URL 修改和本地上传
- ✅ 支持导出编辑后的 HTML
- ✅ Streamlit Cloud 部署支持

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License

---

## 📧 联系方式

如有问题，请通过以下方式联系：
- GitHub Issues
- Email: your-email@example.com

---

**Happy Editing! ✨**
