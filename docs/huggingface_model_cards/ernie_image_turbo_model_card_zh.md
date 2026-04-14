---
license: apache-2.0
pipeline_tag: text-to-image
library_name: diffusers
tags:
  - text-to-image
---

# ERNIE-Image-Turbo

<p align="center">
  <img src="mosaic.jpg" alt="ERNIE-Image Mosaic" width="60%">
</p>

<p align="center">
  <a href="https://huggingface.co/Baidu/ERNIE-Image">🤗 ERNIE-Image</a> &nbsp;|&nbsp;
  <a href="https://huggingface.co/Baidu/ERNIE-Image-Turbo">🤗 ERNIE-Image-Turbo</a> &nbsp;|&nbsp;
  <a href="TODO">💻 GitHub</a> &nbsp;|&nbsp;
  <a href="TODO">📖 Blog</a> &nbsp;|&nbsp;
  <a href="TODO">🖼️ Gallery</a>
</p>

ERNIE-Image-Turbo 是由百度 ERNIE-Image 团队开发的一款开源文生图模型，也是 ERNIE-Image 的蒸馏版本。它延续了同一系列的单流 Diffusion Transformer（DiT）架构，面向更高效的推理速度设计，在仅需 8 个 inference steps 的情况下，仍然保持了较强的画质与可控性。在真实使用场景中，ERNIE-Image-Turbo 依然能够较好地兼顾内容准确性与视觉表现，尤其在复杂指令跟随、文字渲染和结构化图像生成方面保持了较强能力，因此适合海报、漫画、多面板布局等同时关注效果与效率的内容生产场景。同时，模型也覆盖了从写实摄影、设计感图像到风格化表达在内的多种视觉风格。

**技术亮点：**
- **速度与效果兼顾**：作为 ERNIE-Image 的蒸馏版本，ERNIE-Image-Turbo 在仅需 8 个 inference steps 的前提下，依然能够提供较强的生成质量，适合对时延更敏感的应用场景。
- **文字渲染能力强**：ERNIE-Image-Turbo 在高密度文本、长文本以及对版式敏感的文字生成任务上表现稳定，适合海报、信息图、类 UI 图像等重文字场景。
- **指令跟随鲁棒**：对于包含多主体关系、复杂细节约束和知识密集型描述的 prompt，模型能够保持较强的理解与执行能力。
- **结构化生成突出**：在海报、漫画、分镜、故事板和多面板图像等结构化视觉任务中，ERNIE-Image-Turbo 也能较好地保持布局逻辑和画面组织。
- **风格覆盖广**：除了清晰、易读的设计向输出之外，模型也支持写实摄影和辨识度较强的风格化视觉表达，包括更柔和、更具电影感的画面风格。
- **部署友好**：得益于较紧凑的模型规模，ERNIE-Image-Turbo 可以运行在 24G VRAM 的消费级 GPU 上，降低了研究、下游使用和模型适配的门槛。

## 发布版本

### [ERNIE-Image](https://huggingface.co/Baidu/ERNIE-Image): 我们的**SFT模型，**可在**50个推理步骤**内提供更强大的通用能力和指令遵循效果。

### [ERNIE-Image-Turbo](https://huggingface.co/Baidu/ERNIE-Image-Turbo): 我们的**Turbo模型，**通过**DMD和RL**优化，仅需**8个推理步骤**即可实现更快的速度和更高的美观度。

## Benchmark

### GENEval

| 模型 | Single Object | Two Object | Counting | Colors | Position | Attribute Binding | Overall |
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

| 模型 | Alignment | Text | Reasoning | Style | Diversity | Overall |
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

| 模型 | Alignment | Text | Reasoning | Style | Diversity | Overall |
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

| 模型 | LongText-Bench-EN | LongText-Bench-ZH | Avg |
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

## 快速开始

### 推荐参数
- Resolution: 
    - 1024x1024
    - 848x1264
    - 1264x848
    - 768x1376
    - 896x1200
    - 1376x768
    - 1200x896
- Guidance scale: 4.0
- Inference steps: 50

### Diffusers

`pip install git+https://github.com/huggingface/diffusers`

```python
import torch
from diffusers import ErnieImagePipeline

pipe = ErnieImagePipeline.from_pretrained(
    "Baidu/ERNIE-Image-Turbo",
    torch_dtype=torch.bfloat16,
).to("cuda")

image = pipe(
    prompt="一张赛博朋克风格的未来城市电影海报，霓虹招牌文字清晰可读。",
    height=1024,
    width=1024,
    num_inference_steps=8,
    guidance_scale=1.0,
    use_pe=True # use prompt enhancer
).images[0]

image.save("output.png")
```

### SGLang

安装sglang:
```
git clone https://github.com/sgl-project/sglang.git
```

启动服务：

```bash
sglang serve --model-path baidu/ERNIE-Image-Turbo
```

发送生成请求：

```bash
curl -X POST http://localhost:30000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一只黑白相间的中华田园犬",
    "height": 1024,
    "width": 1024,
    "num_inference_steps": 8,
    "guidance_scale": 1.0,
    "use_pe": true
  }' \
  --output output.png
```
