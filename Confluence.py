import sys
from atlassian import Confluence


# Gather our code in a main() function
def main():
    #Class for custom Error
    class UpdateError(Exception):
        pass

    url = 'http://localhost:8090'
    #Entered arguments
    username = sys.argv[1]
    password = sys.argv[2]
    parent_page_url = sys.argv[3]
    need_update = sys.argv[4]

    #Add a connection
    confluence = Confluence(
        url=url,
        username=username,
        password=password)

    parent_page_title = parent_page_url.rpartition('/')[2].replace('+',' ')
    space = parent_page_url.rpartition('/')[0].rpartition('/')[2]
    #If page already exists and user doesn’t want to update then raise error
    if need_update == 'F':
        page_exists = confluence.page_exists(space, parent_page_title)
        if page_exists == True:
            raise UpdateError
    
    first_table_content = [['Name', 'File Name', 'Comment'], ['Test 1', 'Attached text file in txt format (display in url)','This is test one'], ['Test 2', 'Attached text file in txt format (display in url)', 'This is test two']]
    first_table_html = '<table cellspacing="0" style="border-collapse:collapse; border:solid black 1.0pt"><tbody>'
    for row in first_table_content:
        first_table_html=first_table_html+"<tr>"
        for elem in row:
            first_table_html=first_table_html+'<td>'+elem+'</td>'
        first_table_html=first_table_html+"</tr>"
    first_table_html=first_table_html+"</tbody></table>"   

    second_table_content = [['Title', 'Current', 'New', 'Comment'], ['This is test 1', '123','789', '<p>Different</p><ul><li>Abc</li><li>Cdm</li></ul>'], ['This is test 2', '456', '123', 'This is good'], ['This is test 3', '789', '456', 'This bad']]
    second_table_html = '<table cellspacing="0" style="border-collapse:collapse; border:solid black 1.0pt"><tbody>'
    for row in second_table_content:
        second_table_html=second_table_html+"<tr>"
        for elem in row:
            second_table_html=second_table_html+'<td>'+elem+'</td>'
        second_table_html=second_table_html+"</tr>"
    second_table_html=second_table_html+"</tbody></table>"  
        

    new_page_title = 'THIS IS TESTING'
    body = '<p style="color:red;">This is testing 12345</p>' \
           '<h1>Test 1</h1>' + first_table_html + '<h1>Test 2</h1>' + second_table_html

    parent_id = confluence.get_page_id(space, parent_page_title)

    # Update page or create page if it is not exists
    output = confluence.update_or_create(parent_id, new_page_title, body, representation='storage')
    if output:
        new_page_URL=url+'/display/'+space+'/'+new_page_title.replace(' ','+')
    print(new_page_URL)

if __name__ == '__main__':
  main()
