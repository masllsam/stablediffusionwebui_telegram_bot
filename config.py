import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SD_URL = os.environ.get("SD_URL")
ALLOWED_CHATS = []

PAYLOAD = {
    "enable_hr": "false",
    "denoising_strength": "0",
    "firstphase_width": "0",
    "firstphase_height": "0",
    "hr_scale": "2",
    "hr_second_pass_steps": "0",
    "hr_resize_x": "0",
    "hr_resize_y": "0",
    "prompt": "",
    "seed": "-1",
    "subseed": "-1",
    "subseed_strength": "0",
    "seed_resize_from_h": "-1",
    "seed_resize_from_w": "-1",
    "batch_size": "4",
    "n_iter": "1",
    "steps": "5",
    "cfg_scale": "7",
    "width": "512",
    "height": "512",
    "restore_faces": "false",
    "tiling": "false",
    "do_not_save_samples": "false",
    "do_not_save_grid": "false",
    "negative_prompt": "",
    "eta": "0",
    "s_churn": "0",
    "s_tmax": "0",
    "s_tmin": "0",
    "s_noise": "1",
    "override_settings": {},
    "override_settings_restore_afterwards": "true",
    "script_args": [],
    "sampler_index": "Euler",
    "send_images": "true",
    "save_images": "true",
    "alwayson_scripts": {},
}
