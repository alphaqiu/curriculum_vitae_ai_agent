cv_header_template = """
# 要使用的模板
```
<div id='nameBlock' class='largeFont'>
    <span class='myname'>[name]</span><br>
    <span class='label'><b>[gender]</b> ※ <b>[work_experience]</b>工作经验</span>
</div>
<div id='basicsBlock' class='smallFont'>
    <div class='contactBlock'>
        <span class='phone'>[mobile_phone]</span><br>
        <a href="mailto:[email]">[email]</a><br>
        <a href="[github]">[github]</a><br>
        <span class='address'>毕业院校：[education_background]</span>
    </div>
</div>
<div class='sectionLine'></div>
<div id="job_seeking_status" class="sectionBlock">
    <div class='sectionName'>
        <span>基本信息</span>
    </div>
    <div class='sectionContent'>
        <div class='myselfBlock'>
            <span>求职状态：<b>[job_seeking_status]</b></span><br/>
            <span>求职意向：<b>[job_seeking_position]</b></span><br/>
            <span>期望薪资：<b>[job_seeking_salary]</b></span>
        </div>
    </div>
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""

cv_personal_advantage_template = """
# 要使用的模板
```
<div id='myself' class="sectionBlock">
    <div class='sectionName'>
        <span>个人优势</span>
    </div>
    <div class='sectionContent'>
        <div class='myselfBlock'>
            <span>[personal_advantage]</span>
        </div>
    </div>
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""

cv_work_experience_template = """
# 要使用的模板
```
<div id='workBlock' class="sectionBlock">
    <div class='sectionName'>
        <span>工作经历</span>
    </div>
    <div class='sectionContent'>
        <div class='jobBlock'>
            <div class='blockHeader'>
                <span class='title'>[company] - [position]</span>
                <span class='date'>[start_date] &mdash; [end_date]</span>
            </div>
            <p class='highlights'>
                <h3>[work_experience]</h3>
            </p>
            <ul class='details'>
                <li>[work_experience_description]</li>
            </ul>
            <div class='separator'></div>
        </div>
    </div>
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""

cv_project_experience_template = """
# 要使用的模板
```
<div id='projectBlock' class="sectionBlock">
    <div class='sectionName'><span>项目经历</span></div>
    <div class='sectionContent'>
        <div class="jobBlock">
            <div class='blockHeader'>
                <span class='title'>
                    [project_name] - [project_role]
                </span>
                <span class='date'>
                    [project_start_date] &mdash; [project_end_date]
                </span>
            </div>
            <div class='website'>
                <a href='[project_link]'>[project_link]</a>
            </div>
            <p>[project_description]</p>
            <ul class='details'>
                <li>[project_achievements</li>
            </ul>
            <div class='separator'></div>
        </div>
    </div>
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""

cv_education_experience_template = """
# 要使用的模板
```
<div id='educationBlock' class="sectionBlock">
    <div class='sectionName'><span>教育经历</span></div>
    <div class='sectionContent'>
        <div class='jobBlock'>
            <div class='blockHeader'>
                <span class='title'>[school]</span>
            </div>
            <div>
                <h3>[major] - [degree]
                <span class='date'>
                    [start_date] &mdash; [graduation_date]
                </span>
                </h3>    
            </div>
        </div>
    </div>
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""

cv_interest_template = """
# 要使用的模板
```
<div id='interests' class="sectionBlock">
    <div class='sectionName'><span>兴趣爱好</span></div>
    <div class='sectionContent'>
        <ul>
            <li class='name'>[hobbies_and_interests_description]</li>
        </ul>
    </div> 
</div>
<div class='sectionLine'></div>
```

# 输出格式
结果应以 html 格式提供，仅提供简历的 html 代码，不作任何解释或附加文本，并且不带 ```html```
"""
