from splinter.browser import Browser

def main():
    b = Browser('chrome')
    b.driver.set_window_size(1600, 1000)
    url = 'https://www.baidu.com/'
    b.visit(url)
    if b.is_text_present(u'关于百度'):
        print("yes, found it!")
    else:
        print("no, did not found it!")
    b.fill('wd', 'splink')
    third_found = b.find_by_id(u'su').click()

if __name__ == '__main__':
    main()
