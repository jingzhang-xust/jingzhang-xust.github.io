# jemdoc Personal Academic Homepage Starter

这是一套适合硕士生、博士生、科研人员的 GitHub Pages + jemdoc 学术主页模板。

页面结构：

- Home
- Publications
- Projects
- Biography

它同时支持：

- jemdoc 源文件
- jemdoc+MathJax
- 自定义响应式 CSS
- 本地构建
- GitHub Actions 自动构建与发布

## 1. 先修改这些内容

在所有 `.jemdoc` 和 `MENU` 文件里搜索并替换：

- `YOUR NAME`
- `YOUR_USERNAME`
- `XXX University`
- `School of XXX`
- `your.name@university.edu`
- 研究方向
- 教育经历
- 论文与项目
- Google Scholar / GitHub / ORCID 链接

## 2. 替换头像

模板默认使用：

`assets/profile.svg`

你可以直接换成自己的照片，例如：

`assets/profile.jpg`

然后把 `index.jemdoc` 中：

`assets/profile.svg`

改为：

`assets/profile.jpg`

## 3. 本地安装 jemdoc+MathJax

需要电脑已经安装 Git 和 Python 3。

运行：

```bash
python setup_jemdoc.py
```

这个脚本会把 jemdoc+MathJax 下载到：

```text
vendor/jemdoc_mathjax/
```

## 4. 本地构建

运行：

```bash
python build.py
```

生成的网站会放在：

```text
_site/
```

本地预览：

```bash
python -m http.server 8000 -d _site
```

浏览器打开：

```text
http://localhost:8000
```

## 5. 创建 GitHub 主页仓库

假设 GitHub 用户名是：

```text
yourname
```

则仓库名称创建为：

```text
yourname.github.io
```

把本模板中的全部文件上传到该仓库的 `main` 分支。

## 6. 开启 GitHub Pages

进入仓库：

```text
Settings → Pages → Build and deployment → Source
```

选择：

```text
GitHub Actions
```

模板自带：

```text
.github/workflows/pages.yml
```

以后每次向 `main` 推送修改，GitHub Actions 都会：

1. 拉取 jemdoc+MathJax
2. 把 `.jemdoc` 编译成 `.html`
3. 生成 `_site`
4. 部署到 GitHub Pages

最终主页地址通常是：

```text
https://YOUR_USERNAME.github.io/
```

## 7. 推荐的第一次修改顺序

1. 改 `MENU`
2. 改 `index.jemdoc`
3. 改 `biography.jemdoc`
4. 改 `publications.jemdoc`
5. 改 `projects.jemdoc`
6. 换头像
7. 在 `jemdoc.css` 的 `:root` 中调整主题色
8. Push 到 GitHub

## 8. CV

如果你有简历，把它放到：

```text
files/CV.pdf
```

然后在 `index.jemdoc` 或 `MENU` 中添加：

```text
[files/CV.pdf Curriculum Vitae]
```

## 9. 常用 jemdoc 语法

```text
= 一级页面标题
== 二级标题
=== 三级标题

*粗体*
/斜体/

- 无序列表项目

[https://example.com 链接文字]
```

每个页面顶部这一行用于启用统一菜单：

```text
# jemdoc: menu{MENU}{index.html}
```

不同页面把最后的 HTML 文件名换成对应页面即可。

## 10. 项目结构

```text
.
├── MENU
├── index.jemdoc
├── publications.jemdoc
├── projects.jemdoc
├── biography.jemdoc
├── mysite.conf
├── jemdoc.css
├── setup_jemdoc.py
├── build.py
├── assets/
│   ├── profile.svg
│   └── README.md
├── files/
│   └── README.md
├── vendor/
│   └── README.md
└── .github/
    └── workflows/
        └── pages.yml
```

## 上游依赖

本模板使用 `wsshin/jemdoc_mathjax` 作为 jemdoc 编译器来源。上游项目基于 jemdoc，并支持 MathJax 与 Python 3。

本模板自身的文件采用 MIT License；上游 jemdoc/jemdoc+MathJax 的许可条款独立适用。
