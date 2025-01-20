<!doctype html>
<html>
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, user-scalable=no, minimal-ui'>
    <title>$name</title>
    <style>
        body {
            background: #EEEEEE;
            font: 15px "Times New Roman", Times, sans-serif;
            line-height: 1.4;
            margin: 40px 0;
        }

        em {
            /* color: #999; */
            color: #a52a2a;
            font-weight: bold;
        }

        p {
            line-height: 1.4;
        }

        ul {
            margin-bottom: 0;
        }

        li {
            margin-bottom: 2px;
        }

        a {
            text-decoration: none;
        }

        #resume {
            margin: 0 auto;
            max-width: 700px;
            padding: 80px 100px;
            background: #fff;
            border: 1px solid #ccc;
            box-shadow: 2px 2px 4px #aaa;
            -webkit-box-shadow: 2px 2px 4px #aaa;
        }

        .coursesList {
            width: 28%;
            vertical-align: top;
            display: inline-block;
        }

        .largeFont {
            font-size: 20px;
        }

        .smallFont {
            font-size: 13px;
        }

        .sectionBlock {
            display: flex;
            width: 100%;
        }

        .sectionName {
            width: 18%;
            vertical-align: top;
            display: inline-block;
        }

        .sectionContent {
            width: 80%;
            vertical-align: top;
            display: inline-block;
        }

        .sectionContent ul {
            padding-left: 20px;
            margin-top: 6px;
            list-style-type: circle;
        }

        .sectionContent .title {
            font-weight: bold;
        }

        .sectionContent .date {
            float: right;
        }

        .sectionContent .separator {
            height: 8px;
        }

        /* 公司名称块 */
        .blockHeader {
            font: 18px "Times New Roman", Times, sans-serif;
            color: brown;
        }


        .sectionLine {
            border-style: dashed;
            border-width: 1px;
            border-color: #CFCFCF;
            margin-top: 10px;
            margin-bottom: 10px;
        }

        .divider {
            font-weight: bold;
            margin-left: 5px;
            margin-right: 5px;
        }

        .summary {
            margin-top: 6px;
        }

        .skillBlock {
            margin-bottom: 4px;
        }

        .jobBlock {
            page-break-inside: avoid;
        }

        /* Media Queries */
        @media only screen and (max-width: 40em) {
            body {
                margin: 0;
                font-size: 14px;
            }

            #resume {
                margin: 0 auto;
                max-width: 600px;
                padding: 0.5em 1em;
                border: none;
            }

            .sectionBlock {
                flex-direction: column;
            }

            .sectionContent {
                width: 100%;
            }

            .sectionContent .date {
                padding-right: 2em;
            }

            .sectionName {
                width: auto;
            }

            .largeFont {
                font-size: 20px;
            }

            .smallFont {
                font-size: 14px;
            }
        }

        @media print {
            body {
                background: #FFFFFF;
            }

            #resume {
                margin: 0 auto;
                max-width: 600px;
                padding: 0px 0px;
                border: 0px;
                /* background: #fff; */
                background: #fefefe;
                box-shadow: none;
                -webkit-box-shadow: none;
            }

            a {
                color: black;
            }
        }

        #nameBlock {
            float: left;
        }

        #basicsBlock {
            float: right;
        }

        .sectionLine {
            clear: both;
        }


        .sectionName {
            font-size: 20px;
            color: brown
        }

        .myname {
            font-size: 40px;
            font-weight: bold;
            color: brown;
            font-family: cursive;
        }

        .label {
            font-size: 16px;
        }

        #basicsBlock.smallFont {
            font-size: 15px;
        }

        .sectionContent .title {
            font-weight: bold;
            /* font-size: 20px; */
        }

        a:hover {
            background-color: #ba0018;
            color: #fff;
        }

        h3 {
            display: block;
            font-size: 1.1em;
            margin-block-start: 0.3em;
            margin-block-end: 0.3em;
            margin-inline-start: 0px;
            margin-inline-end: 0px;
            font-weight: bold;
        }
    </style>
</head>
    <div id='resume'>
        $body
        <div id='thanks' class="sectionBlock">
            <div class='sectionName'>
                <span>诚挚致谢</span>
            </div>
            <div class='sectionContent'>
                <div class='thanksBlock'>
                    <em><span style="font-size: large;" class='title'>感谢您在百忙中阅读我的简历，期待有机会与您共事。 </em></span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>