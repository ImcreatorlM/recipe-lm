20261114  家庭菜谱助手 - 学习笔记 (V1.0)

#### 🚀 一、日常启动三板斧（最常用）

如果下次想打开网页看菜谱，只需要在终端依次输入：

1. `cd ~/Desktop/recipe-app` （进入项目文件夹）
2. `source venv/bin/activate` （如果你后来建了虚拟环境，没建就不写这句）
3. `python3 -m streamlit run app.py`  
   *（注意：终端要一直开着，看到 `Local URL` 后，去浏览器打开 `localhost:8501`）*

#### ⚠️ 二、我的专属避坑指南（血泪教训）

> **下次如果再遇到这些报错，不要慌，直接查这里：**

- **报错 `command not found: pip` 或 `streamlit`**
  - **原因**：Mac 系统找不到命令。
  - **解药**：永远记住用 `python3 -m pip` 和 `python3 -m streamlit` 开头。
- **报错 `Connection error` (网页连不上)**
  - **原因**：后台服务没开，或者终端被关掉了。
  - **解药**：看终端有没有跑 `python3 -m streamlit run app.py`，跑着就别关终端。
- **GitHub 报错 `Invalid username or token` 或 `403`**
  - **原因**：GitHub 早就不认密码了。
  - **解药**：去 GitHub 生成 Personal Access Token (PAT) 当密码用。
- **GitHub 报错 `HTTP2 framing layer` 或一直连不上**
  - **原因**：国内网络环境问题。
  - **解药**：终端执行 `git config --global http.version HTTP/1.1`。
- **致命错误：Key 泄露**
  - **教训**：`.env` 必须放在 `.gitignore` 里，绝不能手滑粘进 `README.md` 等要公开的文件里。

#### 🧠 三、核心逻辑一句话记住

**`app.py`** 负责画网页（前端） ➡️ **`recipe_json.py`** 负责调大模型并把返回的文本清洗成 JSON 数据（后端） ➡️ **`.env`** 负责藏密码。

#### 📌 四、下次继续的待办 (Next Steps)

- □  给网页加一个“🎲 随机来一道”的按钮。
- □  把食材列表变成好看的表格样式。
- □  如果新增了修改，记得执行 `git add .` ➡️ `git commit -m "说明"` ➡️ `git push`同步到 GitHub。

---

### 💡 记录笔记的两个小建议：

1. **用 Markdown 格式写**：就像上面这样，用 `#` 号写标题，用 `-` 写列表。你可以直接在项目里建一个 `NOTE.md`，以后传 GitHub 也能直接看。
2. **按“场景”记，不按“时间”记**：不要写“今天学了什么”，而是写“启动项目怎么弄”、“怎么推代码”。因为下次你需要的不是历史，而是**操作手册**。
