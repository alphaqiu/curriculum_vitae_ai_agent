# Curriculum Vitae AI Agent

🤖 人工智能求职助手，有针对性的调整简历，助你快速找到心仪的工作。

## Features

- 更符合**中国**境内的习惯
- 针对输入的岗位招聘链接，有针对性地分析岗位3个最重要的职责
- 有针对性地突出个人重点优势
- 量化过往工作指标
- 面向 ATS（Applicant Tracking System）友好的格式
- 可自定义简历模版
- 开箱可用的简历默认模版风格
- 支持多种API接入
- 支持langsmith可观测

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/alphaqiu/curriculum_vitae_ai_agent.git
    cd curriculum_vitae_ai_agent
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To generate a resume, use the following command:

```bash
python main.py --link "https://example.com/job-description" --config "./data/config.yml"
```

- `--link` or `-l`: The URL of the job description (required).
- `--config` or `-c`: Path to the configuration file (optional, defaults to `./data/config.yml`).

## Configuration

The configuration file (`config.yml`) contains settings for the resume generation process, including model usage and file paths. Customize it according to your needs.

### Resume Information

Resume information file is located at `data/info.yml`, you can customize it or use the default information.

### Resume Template

Resume template file is located at `data/resume_templates/resume_template.tpl`, you can customize it or use the default template.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
