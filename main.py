import argparse
from pathlib import Path

from loguru import logger

from src.config import load_config
from src.resume_generator import ResumeGenerator


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="AI简历生成器")
    parser.add_argument(
        "--link",
        "-l",
        type=str,
        help="职位描述链接(必填)",
    )
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default="./data/config.yml",
        help="配置文件路径(可选，默认为 ./data/config.yml)",
    )
    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()
    if args.link == "":
        raise ValueError("职位描述链接不能为空")

    # 检查配置文件路径
    config_path = Path(args.config)
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")

    # 加载配置并生成简历
    config = load_config(str(config_path))
    logger.debug("配置文件加载成功, 开始生成简历")
    resume_generator = ResumeGenerator(config)
    html_content = resume_generator.generate_resume(args.link)
    digest = resume_generator.generate_digest(args.link)
    html_path = resume_generator.generate_html_resume(digest, html_content)
    resume_generator.generate_pdf_resume(html_path)
    resume_generator.driver_quit()
    logger.info("简历生成成功")


if __name__ == "__main__":
    main()
