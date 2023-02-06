from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import index, AddExp, EditExp, deleteExp

class TestUrls(SimpleTestCase): 

    def testIndexView(self): 
        url = reverse('core:index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def testAddView(self): 
        url = reverse('core:add')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddExp)

    def testEditView(self): 
        url = reverse('core:edit', args=["1"])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, EditExp)

    def testDeleteView(self): 
        url = reverse('core:delete', args=["1"])
        print(resolve(url))
        self.assertEquals(resolve(url).func, deleteExp)

