<div align="center">
<h1> ERNIE-Image </h1>
</div>
<p align="center">
  <a href="https://huggingface.co/Baidu/ERNIE-Image">🤗 ERNIE-Image</a> &nbsp;|&nbsp;
  <a href="https://huggingface.co/Baidu/ERNIE-Image-Turbo">🤗 ERNIE-Image-Turbo</a> &nbsp;|&nbsp;
  <a href="https://huggingface.co/spaces/baidu/ERNIE-Image">🤗 ERNIE-Image-Turbo Huggingface Online Demo</a> &nbsp;|&nbsp;
  <a href="https://sandbox-aistudio.baidu.com/ernieimage">🤗 ERNIE-Image-Turbo Baidu AI Studio Online Demo</a> &nbsp;|&nbsp;
  <a href="https://yiyan.baidu.com/blog/posts/ernie-image">📖 Blog</a> &nbsp;|&nbsp;
  <a href="https://ernieimageprompt.com/">🖼️ Art Gallery</a>
</p>

ERNIE-Image is an open text-to-image generation model developed by the ERNIE-Image team at Baidu. It is built on a single-stream Diffusion Transformer (DiT) and paired with a lightweight Prompt Enhancer that expands brief user inputs into richer structured descriptions. With only 8B DiT parameters, it reaches state-of-the-art performance among open-weight text-to-image models.

![mosaic-ernie-image](https://github.com/user-attachments/assets/7797c3e6-87ef-4b53-b70e-446692fc6bdd)


**Highlights:**

- **Compact but strong**: Despite its compact 8B DiT scale, ERNIE-Image remains highly competitive with substantially larger open-weight models across a range of benchmarks.
- **Text rendering**: Performs particularly well on dense, long-form, and layout-sensitive text, making it a strong choice for posters, infographics, UI-like images, and other text-heavy visual content.
- **Instruction following**: Able to follow complex prompts involving multiple objects, detailed relationships, and knowledge-intensive descriptions with strong reliability.
- **Structured generation**: Especially effective for structured visual tasks such as posters, comics, storyboards, and multi-panel compositions.
- **Style coverage**: Supports realistic photography, design-oriented imagery, and distinctive stylized aesthetics.
- **Practical deployment**: Can run on consumer GPUs with 24G VRAM.

## Released Versions

| Model | Description | Inference Steps | CFG |
|-------|-------------|-----------------|-------|
| [ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image) | SFT model with stronger general-purpose capability and instruction fidelity | 50 steps | 4.0 |
| [ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo) | Turbo model optimized by DMD and RL for faster speed and higher aesthetics | 8 steps | 1.0 |

## Benchmark

### GenEval

| Model | Single Object | Two Object | Counting | Colors | Position | Attribute Binding | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| ERNIE-Image (w/o PE) | **1.0000** | 0.9596 | 0.7781 | 0.9282 | 0.8550 | **0.7925** | **0.8856** |
| ERNIE-Image (w/ PE) | 0.9906 | 0.9596 | 0.8187 | 0.8830 | **0.8625** | 0.7225 | 0.8728 |
| Qwen-Image | 0.9900 | 0.9200 | **0.8900** | 0.8800 | 0.7600 | 0.7700 | 0.8683 |
| ERNIE-Image-Turbo (w/o PE) | **1.0000** | **0.9621** | 0.7906 | 0.9202 | 0.7975 | 0.7300 | 0.8667 |
| ERNIE-Image-Turbo (w/ PE) | 0.9938 | 0.9419 | 0.8375 | 0.8351 | 0.7950 | 0.7025 | 0.8510 |
| FLUX.2-klein-9B | 0.9313 | 0.9571 | 0.8281 | 0.9149 | 0.7175 | 0.7400 | 0.8481 |
| Z-Image | **1.0000** | 0.9400 | 0.7800 | **0.9300** | 0.6200 | 0.7700 | 0.8400 |
| Z-Image-Turbo | **1.0000** | 0.9500 | 0.7700 | 0.8900 | 0.6500 | 0.6800 | 0.8233 |

### OneIG-EN

| Model | Alignment | Text | Reasoning | Style | Diversity | Overall |
|---|---:|---:|---:|---:|---:|---:|
| Nano Banana 2.0 | 0.8880 | 0.9440 | 0.3340 | **0.4810** | **0.2450** | **0.5780** |
| Seedream 4.5 | 0.8910 | **0.9980** | 0.3500 | 0.4340 | 0.2070 | 0.5760 |
| ERNIE-Image (w/ PE) | 0.8678 | 0.9788 | **0.3566** | 0.4309 | 0.2411 | 0.5750 |
| Seedream 4.0 | **0.8920** | 0.9830 | 0.3470 | 0.4530 | 0.1910 | 0.5730 |
| ERNIE-Image-Turbo (w/ PE) | 0.8676 | 0.9666 | 0.3537 | 0.4191 | 0.2212 | 0.5656 |
| ERNIE-Image (w/o PE) | 0.8909 | 0.9668 | 0.2950 | 0.4471 | 0.1687 | 0.5537 |
| Z-Image | 0.8810 | 0.9870 | 0.2800 | 0.3870 | 0.1940 | 0.5460 |
| Qwen-Image | 0.8820 | 0.8910 | 0.3060 | 0.4180 | 0.1970 | 0.5390 |
| ERNIE-Image-Turbo (w/o PE) | 0.8795 | 0.9488 | 0.2913 | 0.4277 | 0.1232 | 0.5341 |
| FLUX.2-klein-9B | 0.8871 | 0.8657 | 0.3117 | 0.4417 | 0.1560 | 0.5324 |
| Qwen-Image-2512 | 0.8760 | 0.9900 | 0.2920 | 0.3380 | 0.1510 | 0.5300 |
| GLM-Image | 0.8050 | 0.9690 | 0.2980 | 0.3530 | 0.2130 | 0.5280 |
| Z-Image-Turbo | 0.8400 | 0.9940 | 0.2980 | 0.3680 | 0.1390 | 0.5280 |

### OneIG-ZH

| Model | Alignment | Text | Reasoning | Style | Diversity | Overall |
|---|---:|---:|---:|---:|---:|---:|
| Nano Banana 2.0 | **0.8430** | 0.9830 | **0.3110** | **0.4610** | 0.2360 | **0.5670** |
| ERNIE-Image (w/ PE) | 0.8299 | 0.9539 | 0.3056 | 0.4342 | 0.2478 | 0.5543 |
| Seedream 4.0 | 0.8360 | 0.9860 | 0.3040 | 0.4430 | 0.2000 | 0.5540 |
| Seedream 4.5 | 0.8320 | 0.9860 | 0.3000 | 0.4260 | 0.2130 | 0.5510 |
| Qwen-Image | 0.8250 | 0.9630 | 0.2670 | 0.4050 | **0.2790** | 0.5480 |
| ERNIE-Image-Turbo (w/ PE) | 0.8258 | 0.9386 | 0.3043 | 0.4208 | 0.2281 | 0.5435 |
| Z-Image | 0.7930 | **0.9880** | 0.2660 | 0.3860 | 0.2430 | 0.5350 |
| ERNIE-Image (w/o PE) | 0.8421 | 0.8979 | 0.2656 | 0.4212 | 0.1772 | 0.5208 |
| Qwen-Image-2512 | 0.8230 | 0.9830 | 0.2720 | 0.3420 | 0.1570 | 0.5150 |
| GLM-Image | 0.7380 | 0.9760 | 0.2840 | 0.3350 | 0.2210 | 0.5110 |
| Z-Image-Turbo | 0.7820 | 0.9820 | 0.2760 | 0.3610 | 0.1340 | 0.5070 |
| ERNIE-Image-Turbo (w/o PE) | 0.8326 | 0.9086 | 0.2580 | 0.4002 | 0.1316 | 0.5062 |
| FLUX.2-klein-9B | 0.8201 | 0.4920 | 0.2599 | 0.4166 | 0.1625 | 0.4302 |

### LongTextBench

| Model | LongText-Bench-EN | LongText-Bench-ZH | Avg |
|---|---:|---:|---:|
| Seedream 4.5 | **0.9890** | **0.9873** | **0.9882** |
| ERNIE-Image (w/ PE) | 0.9804 | 0.9661 | 0.9733 |
| GLM-Image | 0.9524 | 0.9788 | 0.9656 |
| ERNIE-Image-Turbo (w/ PE) | 0.9675 | 0.9636 | 0.9655 |
| Nano Banana 2.0 | 0.9808 | 0.9491 | 0.9650 |
| ERNIE-Image-Turbo (w/o PE) | 0.9602 | 0.9675 | 0.9639 |
| ERNIE-Image (w/o PE) | 0.9679 | 0.9594 | 0.9636 |
| Qwen-Image-2512 | 0.9561 | 0.9647 | 0.9604 |
| Qwen-Image | 0.9430 | 0.9460 | 0.9445 |
| Z-Image | 0.9350 | 0.9360 | 0.9355 |
| Seedream 4.0 | 0.9214 | 0.9261 | 0.9238 |
| Z-Image-Turbo | 0.9170 | 0.9260 | 0.9215 |
| FLUX.2-klein-9B | 0.8642 | 0.2183 | 0.5413 |

## Quick Start

### Diffusers

Install the latest version of diffusers:
```
pip install git+https://github.com/huggingface/diffusers
cd diffusers
pip install -e .
```

```python
import torch
from diffusers import ErnieImagePipeline

# Use ERNIE-Image (50 steps)
pipe = ErnieImagePipeline.from_pretrained(
    "baidu/ERNIE-Image",
    torch_dtype=torch.bfloat16,
).to("cuda")

image = pipe(
    prompt="一只黑白相间的中华田园犬",
    height=1024,
    width=1024,
    num_inference_steps=50,
    guidance_scale=4.0,
    use_pe=True
).images[0]

image.save("output.png")
```

For faster generation, use ERNIE-Image-Turbo (8 steps):

```python
pipe = ErnieImagePipeline.from_pretrained(
    "baidu/ERNIE-Image-Turbo",
    torch_dtype=torch.bfloat16,
).to("cuda")

image = pipe(
    prompt="一只黑白相间的中华田园犬",
    height=1024,
    width=1024,
    num_inference_steps=8,
    guidance_scale=1.0,
    use_pe=True
).images[0]
```

### SGLang

### Method 1: Deploy ERNIE-Image with inner Prompt Enhancer (PE) 


Install the latest version of sglang:
```
git clone https://github.com/sgl-project/sglang.git
```

Start the server:

```bash
sglang serve --model-path baidu/ERNIE-Image
```

Send a generation request:

```bash
curl -X POST http://localhost:30000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一只黑白相间的中华田园犬",
    "height": 1024,
    "width": 1024,
    "num_inference_steps": 50,
    "guidance_scale": 4.0
  }' \
  --output output.png
```

### Method 2: Deploy ERNIE-Image and the Prompt Enhancer (PE) separately to improve PE inference speed

Install the latest version of sglang and deloy for ERNIE-Image Server.
```
git clone https://github.com/sgl-project/sglang.git
cd sglang
pip install -e .

sglang serve --model-path baidu/ERNIE-Image-Turbo
```

Install vllm and deploy for ERNIE-Image-PE Server.
```bash
pip install uv
uv venv --python=3.12 --seed
uv pip install vllm
uv pip install transformers==5.4.0

mkdir ./ernie_image_pe
# 将baidu/ERNIE-Image-Turbo目录下的pe和pe_tokenizer子目录文件同步到ernie_image_pe目录下
cp -rfnL ~/.cache/huggingface/hub/models--baidu--ERNIE-Image-Turbo/snapshots/*/pe*/* ./ernie_image_pe
vllm serve ./ernie_image_pe --port 8888
```

Stage1: Get revised prompt:
```bash
curl -X POST http://localhost:8888/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "./ernie_image_pe",
    "messages": [
      {"role": "user", "content": "{\"prompt\": \"一个女孩在海边\", \"width\": 1024, \"height\": 1024}"}
    ],
    "temperature": 0.6,
    "top_p": 0.8,
    "max_tokens": 2048,
    "stream": false
  }'
```

Stage2: Request the DiT model based on the revised prompt:
```bash
curl -X POST http://localhost:30000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {revised_propmt},
    "height": 1024,
    "width": 1024,
    "num_inference_steps": 8,
    "guidance_scale": 1.0,
    "use_pe": false  # Using this method requires use_pe to be false.
  }' \
  --output output.png
```

## Showcase

| Prompt | Image |
|--------|-------|
| <details><summary>展开提示词</summary>一张桌面端浏览器网页界面的截图，宽高比适宜宽屏展示。顶部是标准的浏览器外框区域，左上角的标签页名称显示为 'Introduction to LLMs'，旁边带有细小的关闭叉号。地址栏中显示着网址 'https://www.ai-insights.com/intro-to-llms'，左侧有深灰色的后退、前进和刷新图标，右上角是常规的最小化、最大化和关闭窗口按钮。网页顶部是一个白底导航栏，左侧有一个包含蓝色节点连线图案的品牌Logo，旁边的文字为 'AI Insights'。导航栏中部水平排列着四个导航链接：'Home'、'Models'、'Research' 和 'About Us'。右侧放置着一个带放大镜图标的浅灰色搜索框，以及一个蓝色的 'Log In' 按钮。网页主体部分采用现代简洁的风格，浅灰白色的背景。视觉中心上方是醒目的黑色加粗大标题 'Understanding Large Language Models (LLMs)'，下方紧跟深灰色的副标题 'A brief guide to the AI systems shaping the future of natural language processing.'。页面中下部呈左右两栏布局。左侧为文字说明区，包含一个小标题 'What are LLMs?'，下方正文为 'Large Language Models are advanced artificial intelligence systems designed to understand, generate, and interact with human language. They are trained on vast amounts of text data using deep learning techniques, particularly transformer architectures.'。紧接着是第二个小标题 'How do they work?'，其正文内容为 'By analyzing billions of parameters, LLMs predict the next word in a sequence, allowing them to perform tasks like translation, summarization, and conversation with remarkable accuracy.'。下方还有一个要点列表，标题为 'Key Capabilities:'，包含三个带有圆点符号的项目：'• Text Generation & Completion'，'• Language Translation'，'• Sentiment Analysis'。右侧栏是一幅充满科技感的矢量插画，主色调为深蓝和紫色。插画中心是一个由发光线条和节点构成的大脑形状神经网络，周围环绕着代表不同功能的悬浮图标，包括白色的聊天对话气泡、折角的文档图标以及金色的齿轮。网页最右侧边缘显示着一段灰色的垂直滚动条。画面光线明亮，排版整洁，文字清晰可辨。</summary></details> | <img src="assets/show_cases/showcase1.jpg" width="300"> |
| <details><summary>展开提示词</summary>这是一张夜间城市街道的摄影照片，展示了雨后湿滑路面与昏黄灯光交织的街景。画面主体是一条被雨水打湿的柏油马路，路面因积水呈现出强烈的反光效果，倒映着街道两侧的霓虹灯牌和路灯，形成蓝青色与暖黄色交织的光影。一辆深色轿车正亮着刺眼的白色前大灯行驶在画面右侧的街道上，车灯的光芒在湿润的路面上投射出明亮的倒影。\n\n街道左侧排列着数家店铺，最显眼的是一家挂着黄色招牌的居酒屋，招牌上用醒目的红色和黑色字体写着‘居酒屋’、‘生ビール 190円’以及‘SMOOTH PREMIUM BEER’字样，招牌下方悬挂着一个红色的灯笼。在这家店的上方和侧面还有竖向的灯箱招牌，同样写着‘生ビール 190円’。左侧前景处立着一个小型的发光广告牌，上面列有菜单，隐约可见‘100’等数字。街道右侧是一排较高的建筑物，窗户透出零星灯光，路边竖立着交通标志杆。</summary></details> | <img src="assets/show_cases/showcase3.png" width="300"> |
| <details><summary>展开提示词</summary>画面采用1:1的正方形构图，背景为干净的浅米色，整体呈现出一种现代、简约且充满童趣的扁平矢量插画风格。画面顶部中央是醒目的大号圆润艺术字体标题：'ALPHABET OF CAREERS'，下方紧跟着一行稍小的无衬线副标题：'A Guide to Different Jobs'。 画面主体采用**4行6列的网格布局，其中第一行和第二行各多一个格子**，形成**7-7-6-6的排列结构**，共26个网格整整齐齐地分布在画面中。每个网格为圆角矩形，内包含一个巨大的圆润彩色字母（位于左上角，颜色分别为红色、蓝色、黄色、绿色、橙色、紫色、粉色等）、一个可爱的卡通儿童形象（穿着对应职业服装）以及下方的职业英文标签。 **第一行（A-G，共7个）：** - **A**：穿着白色太空服、戴着透明头盔的女孩 — 'Astronaut' - **B**：穿着白色围裙、戴着高高厨师帽、手中拿着面包的男孩 — 'Baker' - **C**：穿着白色双排扣厨师服、戴着高帽的女孩 — 'Chef' - **D**：穿着白色大褂、戴着蓝色听诊器的男孩 — 'Doctor' - **E**：穿着蓝色工装、戴着黄色安全帽、手中拿着蓝图的男孩 — 'Engineer' - **F**：穿着绿色格子衬衫、戴着草帽和背带裤的男孩 — 'Farmer' - **G**：穿着绿色围裙、戴着园艺手套和遮阳帽、手中拿着浇水壶的女孩 — 'Gardener' **第二行（H-N，共7个）：** - **H**：穿着黑色围裙、手中拿着剪刀和梳子的女孩 — 'Hairdresser' - **I**：穿着沾满颜料的白色罩衣、戴着贝雷帽、手中拿着画笔的男孩 — 'Illustrator' - **J**：穿着黑色法官袍、戴着白色领结、手中拿着法槌的男孩 — 'Judge' - **K**：穿着彩色开衫、手中拿着绘本的温柔女孩 — 'Kindergarten Teacher' - **L**：穿着深蓝色开衫、戴着眼镜、怀中抱着书本的女孩 — 'Librarian' - **M**：穿着黄色背带裤、戴着耳机、手中抱着吉他的男孩 — 'Musician' - **N**：穿着浅绿色手术服、戴着口罩和手术帽的女孩 — 'Nurse' **第三行（O-T，共6个）：** - **O**：穿着黑色制服、戴着警徽帽子的男孩 — 'Officer' - **P**：穿着白色大褂、戴着蓝色手套、手中拿着画笔和调色板的女孩 — 'Painter' - **Q**：穿着紫色围裙、戴着顶针帽子、手中拿着拼布的女孩 — 'Quilter' - **R**：穿着银色工装、戴着护目镜、身边有个小机器人的男孩 — 'Robotics Engineer' - **S**：穿着白色实验服、戴着护目镜、手中拿着烧杯的女孩 — 'Scientist' - **T**：穿着黄色制服、戴着帽子的男孩 — 'Taxi Driver' **第四行（U-Z，共6个）：** - **U**：穿着蓝色潜水服、戴着潜水面罩和脚蹼的男孩 — 'Underwater Explorer' - **V**：穿着绿色手术服、戴着听诊器、怀中抱着小猫的女孩 — 'Veterinarian' - **W**：穿着黑色背心、白色衬衫、戴着围裙、手中托着餐盘的男孩 — 'Waiter' - **X**：穿着白色大褂、戴着蓝色手套、手中拿着X光片的男孩 — 'X-ray Technician' - **Y**：穿着白色海军制服、戴着金色肩章船长帽、手中拿着望远镜的女孩 — 'Yacht Captain' - **Z**：穿着卡其色制服、戴着宽檐帽、身边有小动物的男孩 — 'Zoo Keeper' 整张图表色彩明亮饱和，线条简洁流畅，所有文字均采用无衬线字体且清晰可见，排版严谨对称，具有高度的组织感与教育美感。</summary></details> | <img src="assets/show_cases/showcase5.png" width="300"> |
| <details><summary>展开提示词</summary>这张图片采用了一种非常有创意的“画中画”构图，巧妙地融合了现实摄影与 2D 插画艺术。以下是详细的视觉描述： 1. 核心构图与视觉设计 透视效果： 一部智能手机斜放在白色桌面上。手机屏幕内正显示着一个插画风格的长发漂亮可爱女孩，她像是要从手机屏幕里“走出来”一样，双手捧着一盘真实的叉烧包。 虚实结合： 这种设计模糊了数字世界与现实世界的边界。插画人物是 2D 风格，但她手中的叉烧包、背景中的红苹果、华夫饼和餐具都是真实的摄影图像。 2. 插画人物细节 外貌： 女孩有着浓密的黑色长发，眼神略显好奇。她戴着一顶米色的棒球帽，上面印有 "TEAM OG" 的字样。 穿着： 她穿着棕色的短袖 T 恤，叠穿了粉色的长袖内搭，手腕上戴着一串深绿色的珠串手链。 表情： 她的嘴巴微张，向上凝视，仿佛被手机外的某种美食所吸引。 3. 周边元素与装饰 Emoji 与贴纸： 屏幕周围漂浮着大量的食物 Emoji 和文字贴纸： 食物： 热狗（在云朵里）、蛋糕、蝴蝶酥、汉堡、三明治、甜甜圈。 文字： "RESUUSABLE!"（注：拼写略有偏差）、"SO CHEWY!"、"YUMMY"。 表情符号： 蓝色水滴、吐舌头的搞怪眼睛等。 手机界面： 手机底部显示着典型的相机拍照界面，包括“照片”、“人像”、“全景”等模式切换字样，快门键是醒目的白色圆圈。 4. 现实环境背景 美食： 右上角是几颗鲜红饱满的苹果。右侧盘子里盛着诱人的华夫饼，上面配有煎蛋和培根。 餐具： 左上方斜放着一把白柄叉子，色调简洁干净。 氛围： 整体光线明亮柔和，色调清新，充满了一种现代社交媒体流行的“探店”或“美食日记”的艺术感。</summary></details> | <img src="assets/show_cases/showcase6.png" width="300"> |
| <details><summary>展开提示词</summary>一张彩色手绘风格的二次元Q版LINE表情包贴纸合集图。画面采用4行6列的网格布局，总共展示了24个半身像表情包。整体画风为可爱的日系Q版，线条简洁圆润，色彩明快，底色为纯白。所有表情包的主角为同一名二次元少女，她有着浅粉色的齐刘海短发，头顶戴着标志性的头饰：一对白色的毛茸茸猫耳，以及一个显眼的红色十字架蝴蝶结发带。她身穿简单的蓝白相间水手服。每个表情包旁边都配有手写体简体中文字符，文字带有白色描边或黑底，清晰可见。\n\n第一行从左至右依次为：1. 少女面带微笑，举起右手挥手打招呼，旁边写着'早上好'。2. 少女戴着睡帽闭眼睡觉，鼻尖冒着睡眠泡泡，配文'晚安'。3. 少女歪着头，头上冒出巨大的红色问号，配文'啊？'。4. 少女双手合十，眼泪汪汪地看着前方，配文'拜托拜托'。5. 少女双手握拳，眼神坚定，背景带有集中线，配文'冲鸭！'。6. 少女无奈地摊开双手，叹了一口气，配文'绝了'。\n\n第二行从左至右依次为：1. 少女单手捂嘴偷笑，周围有小花朵特效，配文'嘿嘿嘿'。2. 少女愤怒地拍打面前的桌子，头上带有生气的井字号，配文'生气了！'。3. 少女脸颊通红，双手捂住脸庞，头上冒着蒸汽，配文'太害羞了吧'。4. 少女戴着黑色像素风墨镜，双手抱胸，配文'无所畏惧'。5. 少女手里拿着一把放大镜凑近观察，配文'让我康康'。6. 少女双手捧着一杯珍珠奶茶用吸管喝，表情十分满足，配文'续命成功'。\n\n第三行从左至右依次为：1. 少女平躺在地上，嘴里吐出白色的半透明灵魂，配文'不想努力了'。2. 少女满脸笑容，向前方举起大拇指点赞，配文'绝绝子'。3. 少女坐在地上，抱着一根虚线柱子大哭，眼泪飞溅，配文'带带我'。4. 少女手里拿着一把玩具塑料刀，嘴角露出黑化的腹黑笑容，配文'你再说一遍'。5. 少女全身变成灰色的石像状态，并带有裂纹，配文'心态崩了'。6. 少女开心地向上抛洒彩纸和花瓣，配文'好耶！'。\n\n第四行从左至右依次为：1. 少女双手捧着手机快速打字，满头大汗，黑眼圈明显，配文'在肝了在肝了'。2. 少女双手递出一大束红玫瑰，脸颊微红，配文'送给你'。3. 少女惊恐地双手抱头，瞳孔缩小，背景变暗，配文'危！'。4. 少女双眼变成黄色的星星形状，充满期待，配文'尊嘟假嘟'。5. 少女单手托腮，眼神呆滞，嘴角流出一滴口水，配文'阿巴阿巴'。6. 少女背对画面挥手告别，转头流下一滴眼泪，配文'溜了溜了'。</summary></details> | <img src="assets/show_cases/showcase7.png" width="300"> |
| <details><summary>展开提示词</summary>这是一张从汽车内部向外拍摄的摄影照片，捕捉了黄昏时分的田野景色。画面左侧占据前景的是汽车内部结构，包括部分深色的方向盘轮廓、打开的车门内侧面板以及上方的车窗边框。车门处于开启状态，透过车窗和车门缝隙可以看到外部的自然风光。 画面的主要部分是车外的田野和天空。天空呈现出日落时分的壮丽色彩，地平线附近是浓郁的橙红色余晖，向上逐渐过渡为淡紫色和深蓝色的天空。云层分布不均，有的被夕阳染成粉红色，有的则呈现暗灰色，增加了天空的层次感。地平线上可以看到连绵的深色树林剪影和几个细小的电线杆，表明这是一个乡村或郊野环境。前景的田野处于背光状态，光线昏暗，只能隐约辨认出深绿色的植被和杂草，细节难以看清，整体呈现出一种宁静而略带忧郁的氛围。 光线主要来自远处的夕阳，形成了强烈的明暗对比，车内和近处的田野处于阴影中，而天空则是视觉焦点。画面底部中央叠加了一行白色的英文文字：'And we are"。</summary></details> | <img src="assets/show_cases/showcase8.jpg" width="300"> |
| <details><summary>展开提示词</summary>一张宽幅科普教育信息图，背景为深蓝色，带有浅蓝色的微弱几何网格纹理，整体呈现现代科技与数学结合的3D渲染风格。画面横向分为左、中、右三个逻辑区块，完美适配宽屏构图比例。 画面顶部居中是醒目的白色大字标题 '庞加莱猜想'，其下方有一行浅蓝色的较小副标题 'The Poincaré Conjecture: 拓扑学中的百年难题'。 画面左侧区块通过经典的二维类比解释“单连通”概念。该区域上方绘制了一个逼真的红苹果模型（代表二维球面），其表面套着一条发光的蓝色闭合绳圈，绳圈内部画有两圈逐渐缩小的虚线，带有箭头指向表面的一个蓝色发光点，展示绳圈收缩的过程。苹果右侧排布着三行白色说明文字：'二维球面 (2-Sphere)'、'单连通 (Simply Connected)'、'表面上的任何闭合绳圈都可以连续收缩到一个点'。该区域下方绘制了一个带有3D光影的橙色甜甜圈（代表环面），表面套着一条穿过中间孔洞的发光红色绳圈。甜甜圈右侧写有三行白色文字：'环面 (Torus)'、'非单连通 (Not Simply Connected)'、'穿过孔洞的绳圈被卡住，无法收缩到一个点'。 画面正中间区块展示猜想的核心定理。中央悬浮着一个半透明的、内部交织着复杂发光青色经纬线的球体，用来抽象表现三维球面（3-sphere）。该球体下方悬浮着一个带有半透明磨砂玻璃质感边框的矩形文本框，文本框内居中排布着明黄色的定理文字：'任何一个单连通的、封闭的三维流形一定同胚于三维球面。'，在这行黄色文字正下方紧跟着一行白色英文：'Every simply connected, closed 3-manifold is homeomorphic to the 3-sphere.' 画面右侧区块解释该猜想的证明逻辑。顶部标题文字为亮橙色的 '证明与里奇流 (Ricci Flow)'。标题下方是一组由左至右平滑演变的3D几何体序列：最左侧是一个表面凹凸不平、扭曲且带有类似哑铃状突起的不规则灰色流形；一条向右的渐变黄色箭头指向中间的几何体，该几何体的突起变短、表面坑洼变得部分平滑；另一条向右的箭头指向最右侧的几何体，此时它已经演变成了一个完美、光滑且发光的蓝色球体。在这组渐变演化图的下方，有两段整齐的白色说明文本，第一段为：'2002-2003年，俄罗斯数学家格里戈里·佩雷尔曼证明了该猜想。'，第二段为：'核心方法：利用里奇流方程，像热量扩散一样，将不规则的拓扑空间逐步“平滑化”，最终演变成完美的球面。' 整体构图平衡，信息层级分明，字体无重叠且清晰可读，几何体带有细腻的材质与发光特效，呈现出严谨且直观的科学美感。</summary></details> | <img src="assets/show_cases/showcase9.png" width="300"> |
| <details><summary>展开提示词</summary>盛夏午后的日本社区公园一角，树荫遮蔽下的石凳。石凳上静静放着一个晶莹剔透的玻璃金鱼缸，旁边是一副太阳镜、一个竹制杯垫和一把白色遮阳伞。石凳旁簇拥着盛开的紫蓝色绣球花，背景是略显模糊的向日葵田和社区游泳池的一抹清凉蓝色。画面呈现日系极简摄影美学，空气感十足，色调清新淡雅，光线柔和且略微过曝，阴影处带有清冷的蓝绿色调，高调照明，低对比度，构图洁净，带有细腻的胶片质感和宁静的夏日氛围。</summary></details> | <img src="assets/show_cases/showcase10.png" width="300"> |

### Other Resources
- The latest version of [ComfyUI](https://github.com/comfy-org/ComfyUI) now supports our model.
- [Unsloth](https://github.com/unslothai/unsloth) supports building GGUF weights for our model.
- [AI-Toolkit](https://github.com/ostris/ai-toolkit) supports fine-tuning our model.

## Contacts
If you have any questions or suggestions, please feel free to contact us:

| | |
|---|---|
| WeChat | <img src="assets/contacts/WeChat.jpg" width="120"> |
| Discord | [Discord](https://discord.gg/ByUTbjfG5k) |
| X | [X](https://x.com/ErnieforDevs) |
| Email | [wenxin-all@baidu.com](mailto:wenxin-all@baidu.com) |## Contacts

## Star History

TODO

## License

This project is licensed under the [Apache License 2.0](LICENSE).
