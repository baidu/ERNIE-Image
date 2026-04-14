import torch
import random
from diffusers import ErnieImagePipeline

# 加载 pipeline
pipe = ErnieImagePipeline.from_pretrained(
    "baidu/ERNIE-Image-Turbo",
    torch_dtype=torch.bfloat16,
)
pipe = pipe.to("cuda")

# 设置随机种子
seed = random.randint(0, 10000)
generator = torch.Generator(device="cuda").manual_seed(seed)
# 生成图片
output = pipe(
    prompt="一只黑白相间的中华田园犬",
    height=1024,
    width=1024,
    num_inference_steps=8,
    guidance_scale=1.0,
    generator=generator,
    use_pe=True
)

revised_prompt = output.revised_prompts
images = output.images
for img_id, image in enumerate(images):
    image.save(f"./hf_output_{img_id}.png")
print(revised_prompt)