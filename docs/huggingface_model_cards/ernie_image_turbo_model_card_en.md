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

ERNIE-Image-Turbo is an open text-to-image generation model developed by the ERNIE-Image team at Baidu. It is the distilled release of ERNIE-Image, built on the same single-stream Diffusion Transformer (DiT) family and designed for fast generation with strong fidelity in only 8 inference steps. The model retains strong controllability in practical generation scenarios where accurate content realization matters as much as aesthetics. In particular, ERNIE-Image-Turbo remains strong on complex instruction following, text rendering, and structured image generation, making it well suited for posters, comics, multi-panel layouts, and other content creation tasks that require both visual quality and efficiency. It also supports a broad range of visual styles, including realistic photography, design-oriented imagery, and stylized aesthetic outputs.

**Highlights:**
- **Fast and efficient**: As the distilled checkpoint of ERNIE-Image, ERNIE-Image-Turbo delivers strong generation quality with only 8 inference steps, making it suitable for latency-sensitive applications.
- **Text rendering**: ERNIE-Image-Turbo performs well on dense, long-form, and layout-sensitive text, making it a strong choice for posters, infographics, UI-like images, and other text-heavy visual content.
- **Instruction following**: The model is able to follow complex prompts involving multiple objects, detailed relationships, and knowledge-intensive descriptions with strong reliability.
- **Structured generation**: ERNIE-Image-Turbo is effective for structured visual tasks such as posters, comics, storyboards, and multi-panel compositions, where layout and organization are critical.
- **Style coverage**: In addition to clean and readable design-oriented outputs, the model also supports realistic photography and distinctive stylized aesthetics, including softer and more cinematic visual tones.
- **Practical deployment**: Thanks to its compact size, ERNIE-Image-Turbo can run on consumer GPUs with 24G VRAM, which lowers the barrier for research, downstream use, and model adaptation.

## Released Versions

### [ERNIE-Image](https://huggingface.co/Baidu/ERNIE-Image): Our **SFT model**, delivers stronger general-purpose capability and instruction fidelity in typically **50 inference steps**.

### [ERNIE-Image-Turbo](https://huggingface.co/Baidu/ERNIE-Image-Turbo): Our **Turbo model**, optimized by **DMD and RL**, achieves faster speed and higher aesthetics in only **8 inference steps**.

## Benchmark

### GENEval

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


### Recommended Parameters
- Resolution: 
    - 1024x1024
    - 848x1264
    - 1264x848
    - 768x1376
    - 896x1200
    - 1376x768
    - 1200x896
- Guidance scale: 1.0
- Inference steps: 8


### Diffusers

Install the latest version of diffusers:
```
pip install git+https://github.com/huggingface/diffusers
```


```python
import torch
from diffusers import ErnieImagePipeline

pipe = ErnieImagePipeline.from_pretrained(
    "Baidu/ERNIE-Image-Turbo",
    torch_dtype=torch.bfloat16,
).to("cuda")

image = pipe(
    prompt="A cinematic movie poster of a futuristic city at night with clear neon signage.",
    height=1024,
    width=1024,
    num_inference_steps=8,
    guidance_scale=1.0,
    use_pe=True # use prompt enhancer
).images[0]

image.save("output.png")
```




### SGLang

Install the latest version of sglang:
```
git clone https://github.com/sgl-project/sglang.git
```

Start the server:

```bash
sglang serve --model-path baidu/ERNIE-Image-Turbo
```

Send a generation request:

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
