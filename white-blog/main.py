import render

if __name__ == '__main__':
    r = render.Render(r'./docs_test',
                      r'./site',
                      'web_template.html',
                      'blog_template.html',
                      'card_template.html',
                      'kvrmnks')
    # r.render_markdown_content('dsfsdfsdfsd')
    r.build()
    print(r.blog_list)
