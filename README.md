# crawler_trans

传入英文文章的 URL，翻译成中文，并保存成md文件。
> copilot generate, 20 minutes from start to successful run

系统流程：
URL-》jina reader -》translation agent（Andrew Ng）-》deepseek

## 文件目录

- content_en： 英文原文
- content_zh：中文译文
- src
  - crawler：jina reader 调用
  - translation_agent：Andrew Ng 的翻译 agent
- config.ini：配置文件
- main.py：主程序

## 环境变量

```
config.ini
[DEFAULT]
Authorization = ********
OpenAI_API_KEY = **********
````

or

``` bash
export Authorization = ********
export OpenAI_API_KEY = ********
```

## 运行

```bash
python main.py url
```
