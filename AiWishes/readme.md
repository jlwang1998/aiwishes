# 一、将本地代码上传至git
1、安装 Git‌
确保你的电脑上安装了 Git。你可以从 Git 官网 下载并安装。
‌2、打开终端‌
在 VSCode 中，你可以通过点击顶部菜单的 Terminal > New Terminal 来打开一个新的终端窗口。
3、‌初始化 Git 仓库‌
在终端中，导航到你的项目文件夹，然后运行以下命令来初始化 Git 仓库：
git init
4、‌添加远程仓库‌
你需要知道你的 GitHub 仓库的 URL。然后，运行以下命令来添加远程仓库：
git remote add origin <repository-url>
替换 <repository-url> 为你的 GitHub 仓库的 URL。
5、‌添加并提交你的更改‌
将你的更改添加到暂存区并提交：
git add .
git commit -m "Initial commit"
6、‌推送更改到 GitHub‌
最后，将你的更改推送到 GitHub：
git push -u origin main

# 二、vscode调整pip源
永久调整：
终端输入：
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com

可输入pip config get global.index-url进行验证

# 三、创建项目的.venv虚拟环境
vscode需要先安装python插件，Cmd+Shift+P（macOS）打开命令面板，然后输入Python: Select Interpreter创建虚拟环境即可

# 四、vscode上传git慢，通过代理
配置Git客户端使用代理服务器，可以通过设置HTTPS或HTTP代理来加速上传速度,端口替换为实际代理的端口
`git config –global http.proxy http://127.0.0.1:7890`
`git config –global https.proxy http://127.0.0.1:7890`

取消代理，使用：
` git config --global --unset http.proxy`
`git config --global --unset http.proxy`

# 五、上传github时忽略.venv文件夹
在使用 VSCode 推送代码到 GitHub 时，如果你不想上传依赖库（例如 本项目中的 .venv 文件夹），你可以通过 .gitignore 文件来排除这些文件或文件夹。.gitignore 文件可以帮助你指定哪些文件或文件夹 Git 应该忽略，这样在推送代码时就不会包含这些文件。

步骤 1: 创建或编辑 .gitignore 文件
在项目根目录下，创建一个名为 .gitignore 的新文件
打开 .gitignore 文件进行编辑。

步骤 2: 添加依赖库到 .gitignore
在 .gitignore 文件中，添加你想要忽略的依赖库或文件夹。例如，对于本项目，你可以添加以下内容来忽略 .venv 文件夹：
`.venv/`

注意事项:
已存在的 .venv‌：如果你已经有.venv 文件夹在你的本地仓库中，你需要先从 Git 历史中移除这个文件夹（但不删除本地文件）。这可以通过以下命令完成：

`git rm -r --cached node_modules/`

然后再次提交和推送你的 .gitignore 文件更改。

# 六、数据库mysql安装与配置
https://zhuanlan.zhihu.com/p/1978781019361531662

一、虚拟环境
# 1、创建虚拟环境
# 在项目根目录执行
python -m venv .venv  # .venv 为环境文件夹名（可自定义）
# 2、激活虚拟环境
windows
.\.venv\Scripts\activate
Linux：
source .venv/bin/activate
# 3、VSCode 关联解释器
按 Ctrl+Shift+P → 输入 Python: Select Interpreter。
选择虚拟环境路径（如 ./.venv/Scripts/python.exe）。
右下角状态栏显示当前环境名称即配置成功。

网易邮箱：POP3/SMTP/IMAP授权码：ZLb65ErcR3esQVLP