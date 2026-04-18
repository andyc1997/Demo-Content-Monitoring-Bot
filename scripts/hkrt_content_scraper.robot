*** Settings ***
Library           SeleniumLibrary
Library           DateTime
Library           OperatingSystem
Library           Collections
Library           String

*** Variables ***
${URL}            https://news.rthk.hk/rthk/ch/latest-news.htm
${BROWSER}        Chrome
${DRIVER_PATH}    drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe
${RESULTS_DIR}    results
${LOGS_DIR}       logs

*** Test Cases ***
Extract Top 10 News
    [Documentation]    Extract top 10 news from RTHK latest news and save as JSON
    ${timestamp} =    Get Current Date    result_format=%Y%m%d_%H%M%S
    ${result_file} =    Set Variable    ${RESULTS_DIR}/news_data_${timestamp}.json

    # Create results directory if not exists
    Create Directory    ${RESULTS_DIR}

    # Initialize list to store news data
    ${news_list} =    Create List

    # Open browser
    Open Browser    ${URL}    ${BROWSER}    executable_path=${DRIVER_PATH}
    Maximize Browser Window

    # Wait for page to load
    Wait Until Page Contains Element    xpath=//div[@class='ns2-page']    timeout=10s

    # Extract top 10 news
    ${news_containers} =    Get WebElements    xpath=//div[@class='ns2-page']
    ${count} =    Get Length    ${news_containers}
    ${max_news} =    Set Variable If    ${count} > 10    10    ${count}

    FOR    ${index}    IN RANGE    1    ${max_news}+1
        ${title} =    Get Text    xpath=(//div[@class='ns2-page'])[${index}]//h4[@class='ns2-title']/a/font
        ${date} =    Get Text    xpath=(//div[@class='ns2-page'])[${index}]//div[@class='ns2-created']/font
        ${link} =    Get Element Attribute    xpath=(//div[@class='ns2-page'])[${index}]//h4[@class='ns2-title']/a    href

        # Click the link to open article
        Click Link    ${link}
        
        # Wait for article to load
        Wait Until Page Contains Element    xpath=//div[@class='itemFullText']    timeout=10s
        
        # Extract article content from the detail page
        ${content} =    Get Text    xpath=//div[@class='itemFullText']
        
        # Create news object
        ${news_item} =    Create Dictionary    title=${title}    date=${date}    content=${content}
        
        # Add to list
        Append To List    ${news_list}    ${news_item}
        
        # Go back to main page
        Go Back
        
        # Wait for page to reload
        Wait Until Page Contains Element    xpath=//div[@class='ns2-page']    timeout=10s
    END

    # Close browser
    Close Browser

    # Save to JSON file
    Write JSON To File    ${result_file}    ${news_list}

    Log    News data extracted and saved to ${result_file}

*** Keywords ***
Write JSON To File
    [Arguments]    ${filepath}    ${data}
    [Documentation]    Write data to JSON file using Python
    ${json_str} =    Evaluate    json.dumps(${data}, ensure_ascii=False, indent=2)    json
    Create File    ${filepath}    ${json_str}