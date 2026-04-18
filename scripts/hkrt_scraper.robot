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
    [Documentation]    Extract top 10 news from RTHK latest news
    ${timestamp} =    Get Current Date    result_format=%Y%m%d_%H%M%S
    ${result_file} =    Set Variable    ${RESULTS_DIR}/news_data_${timestamp}.csv

    # Create results directory if not exists
    Create Directory    ${RESULTS_DIR}

    # Create the CSV file with headers
    Create File    ${result_file}    Title,Date\n

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

        # Append to CSV
        Append To File    ${result_file}    "${title}","${date}"\n
    END

    # Close browser
    Close Browser

    Log    News data extracted and saved to ${result_file}