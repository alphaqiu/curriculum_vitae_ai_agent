from src.template_base import (
    cv_education_experience_template,
    cv_header_template,
    cv_interest_template,
    cv_personal_advantage_template,
    cv_project_experience_template,
    cv_work_experience_template,
)

header_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是为简历创建专业且精美的标题。

# 要求：
1. **联系信息**：包括求职人的
- 姓名（name）
- 性别（gender）
- 电话号码（mobile_phone）
- 电子邮件地址（email）
- 毕业院校（education_background）
- 求职状态（job_seeking_status）
- 求职意向（position）
- 期望薪资（salary）

2. **格式**：确保联系信息清晰易读。
3. **求职意向**： 求职意向、期望薪资只能有一个，从我的基本信息中挑选一个，确保使用与求职岗位最恰当的一个。
4. **要实现这一点**：
- 如果未提供任何联系信息字段（例如 GitHub 个人资料）（即“无”），请从标题中删除它们。

# 岗位描述
  {job_description}

# 我的基本信息
  {resume_profile}
"""
    + cv_header_template
)

personal_advantage_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是写出最适合该岗位的个人优势。

# 要求
1. 针对岗位描述、个人优势和岗位关键点，写出最适合该岗位的个人优势。
2. 个人优势需要尽可能全面，不要遗漏任何重要信息。

# 岗位描述
  {job_description}

# 岗位关键点分析
  {job_key_points}

# 个人优势
  {personal_advantage}
"""
    + cv_personal_advantage_template
)

work_experience_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是写出最适合该岗位的工作经历。

# 要求
1. 针对岗位描述、工作经历和岗位关键点，写出最适合该岗位的工作经历。
2. 工作经历需要尽可能全面，不要遗漏任何重要信息。
3. 运用STAR原则来量化应聘者的简历,目的是丰富他的工作职责,着重强调应聘者是如何通过具体的行动来完成这项任务
4. 重点突出：是指根据岗位的要求，将岗位的相关技能、经验、成就放在最显著的位置，并突出关键词
5. 如果工作经历中的工作描述是多条，则每一条都用模版中提供的`<li>`标签包裹

# 岗位描述
  {job_description}

# 岗位关键点分析
  {job_key_points}

# 工作经历
  {work_experience}
"""
    + cv_work_experience_template
)

project_experience_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是写出最适合该岗位的项目经历。

# 要求
1. 针对岗位描述、项目经历和岗位关键点，写出最适合该岗位的项目经历。
2. 项目经历需要尽可能全面，不要遗漏任何重要信息。
3. 如果项目经历中的项目描述是多条，则每一条都用模版中提供的`<li>`标签包裹
4. 重点突出项目当中最中的结果，实施过程，以及项目当中所使用的技术

# 岗位描述
  {job_description}

# 岗位关键点分析
  {job_key_points}

# 项目经历
  {project_experience}
"""
    + cv_project_experience_template
)

education_experience_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是写出最适合该岗位的教育经历。

# 要求
1. 针对岗位描述、教育经历和岗位关键点，写出最适合该岗位的教育经历。
2. 教育经历需要尽可能全面，不要遗漏任何重要信息。
3. 如果教育经历中的教育描述是多条，则每一条都用`<div class='jobBlock'>`标签包裹
4. 如果没有提供教育经历，则不要输出任何内容

# 岗位描述
  {job_description}

# 岗位关键点分析
  {job_key_points}

# 教育经历
  {education_experience}
"""
    + cv_education_experience_template
)

interest_prompt = (
    """# 目标
担任人力资源专家和简历撰写人，专门撰写适合 ATS 格式的简历。您的任务是写出最适合该岗位的兴趣爱好。

# 要求
1. 兴趣爱好需要尽可能全面，不要遗漏任何重要信息。
2. 兴趣爱好需要尽可能简洁，不要出现冗余或不必要的信息
3. 如果兴趣爱好是多条，则每一条都用`<li>`标签包裹
4. 如果没有提供兴趣爱好，则不要输出任何内容

# 兴趣爱好
  {interest}
"""
    + cv_interest_template
)
