import scrapy
import sys



class Baidu_Spider(scrapy.Spider):

    name = 'baidu_spider'
    
    # 输入参数抛出异常 目前有误
    '''
    if len(sys.argv) < 2:
        raise Exception(' 老铁 你还没输入关键词 ！ ')
    if len(sys.argv) > 2:
        raise Exception(' 老铁 你的关键词超过一个了！')
    '''

    '''
    可能有误


    # 获取用户输入
    search = sys.argv[1]
    # 搜索后url
    start_urls = [
        'https://www.baidu.com//s?wd=' + search
    ]
    

    '''

    # 先以 jizhi 进行测试
    start_urls = [
        'https://www.baidu.com//s?wd=jizhi'
    ]

    base_url = 'https://www.baidu.com'

    def parse(self,response):
        result_lst = response.css('div.result c-container ')


        for result in result_lst:
            yield{
                # 标题
            #    'title':result.css('a.t::text').extract_first(),
                # 链接
            #    'url':result.css('a.t::attr(href)').extract_first(),
                # 介绍
                'introduction':result.css('div.c-abstract::text').extract_first()
                
            }
        # 下一页
        #url = self.base_url + response.css('a::attr(href)').extract_first()
        #yield scrapy.Request(url,callback=self.parse)