# Afterwinter · 寒冬之后

2026 秋招主题交互展示网页，2026 Qoder College Creativity Competition 项目。

**网页地址：https://vacancy1016.github.io/2026-Qoder-College-Creativity-Competition/**

## 体验

- 视频首屏、可变双字体、鼠标跟随照片、字重响应与手绘下划线。
- 桌面滚动固定的五张年度卡片，依次剥离、前进，点击查看数据出处。
- 暗色章节、粘性标题、十二张分速上升的照片与惯性悬停。
- 手机布局、键盘操作、数据来源弹窗、减少动态效果支持。

主页面为根目录 `index.html`，直接打开亦可使用。动画库、样式、脚本和四套字体已经嵌入单文件。照片、视频和海报使用远程原始链接，需要联网。

## 开发

编辑 `src/index.html`、`src/style.css` 与 `src/app.js` 后运行：

```sh
python build.py
```

将生成的 `index.html` 一同提交，GitHub Pages 会自动更新。`vendor/` 保存指定版本动画库与字体；`prepare-assets.py` 可重新获取这些资源。构建仅使用 Python 标准库。第三方库原始许可声明保留于相应文件和构建产物。

## 设计与资料

根据用户提供的 Kolibrie recreation prompt 改编为“计算机寒冬”叙事：奶油白、番茄红、Archivo / Playfair 可变字体与 Yellowtail / Titan One。动画使用 GSAP 3.13.0、ScrollTrigger、SplitText、DrawSVGPlugin、InertiaPlugin 和 Lenis 1.3.17。

数据快照截至 2026 年 11 月 17 日。2026 年秋招主要面向 2027 届，页面不使用 2026 届人数替代 2027 届。历届毕业生规模为教育部全国全专业预计值；技术岗位增速是智联招聘 2026 年三季度应届职位同比，经读特报道、21 财经转载，不代表全国录用率或专业失业率。完整链接在页面“来源 / Notes”。

照片来自 Unsplash，仅为氛围配图，不代表真实求职者或其经历。视频与静帧使用用户提供的设计参考素材原始链接，未重新托管。无个人信息采集或跟踪脚本。

## 发布

GitHub Pages：`main` 分支根目录，使用 `.nojekyll` 直接发布静态网页。
