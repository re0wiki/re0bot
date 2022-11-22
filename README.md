# Re:从零开始的异世界生活 Wiki

[![GitHub license](https://img.shields.io/github/license/CCXXXI/re0wiki)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/CCXXXI/re0wiki)](../../commits)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/CCXXXI/re0wiki.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CCXXXI/re0wiki/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/CCXXXI/re0wiki.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CCXXXI/re0wiki/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/ccxxxi/re0wiki/badge)](https://www.codefactor.io/repository/github/ccxxxi/re0wiki)
[![Discord server](https://img.shields.io/discord/779185920670171136?label=discord&logo=discord&logoColor=white)](https://discord.gg/F554jbmEUd)
[![Telegram group](https://img.shields.io/badge/Telegram-re0wiki-blue.svg?logo=telegram)](https://t.me/re0wiki)

用于 [Re:从零开始的异世界生活 Wiki | Fandom](https://rezero.fandom.com/zh) 的一些脚本。

## Deployment

- **本项目**：`git clone --depth 1 --recurse-submodules --shallow-submodules https://github.com/CCXXXI/re0wiki.git`
- **Python**：[conda-forge/miniforge](https://github.com/conda-forge/miniforge#install)
- **requirements**：`mamba env create -f environment.yml`
- [机器人密码 | Re:从零开始的异世界生活 Wiki | Fandom](https://rezero.fandom.com/zh/wiki/Special:BotPasswords)
- **用户配置文件**
  1. [user-config.py#L17](./user-config.py#L17)
  2. 同目录下创建`user-password.py`并填写，格式为`('<UserName>', BotPassword('<BotName>', '<BotPassword>'))`

## Usage

- [pywikibot/scripts at master · wikimedia/pywikibot](https://github.com/wikimedia/pywikibot/tree/master/scripts#readme)
- `bash auto.sh`
- `python main.py -h`
- `python rename.py -h`
