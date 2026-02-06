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
