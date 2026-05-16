# 扩散模型与视觉计算前沿 - 在线考试系统

一个基于纯HTML/CSS/JavaScript的在线考试系统，包含4套完整的考卷，共400道题目，涵盖扩散模型与视觉计算的13个前沿方向。

## 功能特性

- **4套独立考卷**：考卷A/B/C/D，各100题，题目不重复
- **三种题型**：单选题（50题×1分）+ 多选题（30题×1.5分）+ 判断题（20题×0.5分）
- **难度分布**：难:中:易 = 5:3:2
- **120分钟倒计时**：最后10分钟/5分钟变色警告，超时自动交卷
- **答题进度追踪**：左侧题号导航，实时显示已答/未答状态
- **自动保存**：答案实时保存到localStorage，刷新不丢失
- **智能评分**：多选题漏选得0.5分，错选0分
- **成绩报告**：总分 + 各题型得分 + 逐题回顾 + 详细解析
- **键盘快捷键**：方向键翻页，数字键快速选题
- **数学公式渲染**：支持LaTeX公式渲染（KaTeX）

## 知识覆盖

### 13个前沿方向

1. **扩散理论基础**：DDPM、DDIM、Score-based Models、Flow Matching、Rectified Flow、Consistency Models、DPM-Solver++
2. **统一视觉表征**：DINOv2、MAE、CLIP、Swin Transformer、BEiT、REPA
3. **扩散超分辨率**：SR3、StableSR、DiffBIR
4. **3D重建与神经渲染**：NeRF、DreamFusion、3D Gaussian Splatting、Mip-NeRF 360、Instant-NGP
5. **数字人与说话人头像**：RAD-NeRF、SadTalker、GeneFace
6. **语义分割与SOD**：SAM、SAM 2、FastSAM、HQ-SAM
7. **视频生成**：Sora、VideoLDM、AnimateDiff、CogVideoX
8. **时间序列预测**：TimeGrad、TIMEMIXER++
9. **多模态理解与生成**：LLaVA、Qwen-VL、BLIP-2、GPT-4V
10. **低光/恶劣天气图像恢复**：LLFlow
11. **遥感图像分析**：DiffusionSat
12. **模型加速与压缩**：LCM、SDXL-Turbo、DeepCache
13. **跨领域应用**：医学图像、分子设计、音频合成

## 使用方法

### 本地运行

1. 克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/diffusion-exam-system.git
```

2. 打开 `index.html` 文件即可使用

### 部署到GitHub Pages

1. Fork 本仓库
2. 进入仓库设置 → Pages
3. 选择分支和目录，保存
4. 访问 `https://YOUR_USERNAME.github.io/diffusion-exam-system/`

## 项目结构

```
diffusion-exam-system/
├── index.html          # 主应用文件（包含HTML/CSS/JS和数据）
├── README.md           # 项目说明
├── LICENSE             # MIT许可证
└── .gitignore          # Git忽略配置
```

## 技术栈

- **前端**：纯HTML5 + CSS3 + JavaScript（无框架依赖）
- **数学渲染**：KaTeX
- **数据存储**：localStorage（本地持久化）

## 考卷详情

| 考卷 | 总分 | 题量 | 时长 |
|------|------|------|------|
| 考卷A | 105分 | 100题 | 120分钟 |
| 考卷B | 100分 | 100题 | 120分钟 |
| 考卷C | 100分 | 100题 | 120分钟 |
| 考卷D | 100分 | 100题 | 120分钟 |

## 内容准确性

所有题目均基于真实发表的论文，每道题解析注明参考来源：
- 论文作者、年份、会议/期刊信息准确
- 方法原理描述准确，无幻觉内容
- 引用论文包括NeurIPS、ICLR、CVPR、ICCV等顶级会议

## License

MIT License

## 致谢

感谢所有被引用论文的作者们，他们的研究工作构成了本考试系统的知识基础。
