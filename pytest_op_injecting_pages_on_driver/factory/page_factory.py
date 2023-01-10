import inspect
from importlib import import_module
from pkgutil import walk_packages
from selenium.webdriver.support.ui import WebDriverWait


def mappings_wrapper(page):
    def cls_modifier(cls):
        """
            Injecting page identification data, e.g: name, environment, is_component, ...
            if the page not contains is_on_focus, raise error, but the page is not a component!
        """
        # Injecting page identification data
        cls.mapping_name = page
        return cls

    return cls_modifier


def page_wrapper(name):
    def cls_modifier(cls):
        """
            Injecting page identification data, e.g: name, environment, is_component, ...
            if the page not contains is_on_focus, raise error, but the page is not a component!
        """
        # Injecting page identification data
        cls.page_name = name
        return cls

    return cls_modifier


from pytest_op_injecting_pages_on_driver.pages.home import Home


class Pages:
    def __init__(self):
        self.home = Home()
# class PageFactory:
#     """ Load the pages """
#
#     def __init__(self, platform):
#         self._platform = platform.lower()
#         self._pages = []
#         self.load_pages()
#
#     def load_pages(self):
#         pages_dict_ = {}
#         mappings_dict_ = {}
#         if self._platform not in _ALL_SUPPORTED_PLATFORMS:
#             raise TypeError(
#                 f'This platform is not supported, only these: {_ALL_SUPPORTED_PLATFORMS}')
#         package = f'mobile.{self._platform}' if self._platform in _MOBILE_PLATFORM else self._platform
#         modules_pages = import_module(package)
#         for module_info in walk_packages(path=modules_pages.__path__, prefix=f'{modules_pages.__name__}.'):
#             module = import_module(module_info.name)
#             print(module_info.name)
#             for _, obj in inspect.getmembers(module, lambda m: inspect.isclass(m)):
#                 if hasattr(obj, 'mapping_name'):
#                     if obj.mapping_name not in mappings_dict_:
#                         mappings_dict_[obj.mapping_name] = obj
#                 if hasattr(obj, 'page_name'):
#                     if obj.page_name not in pages_dict_:
#                         pages_dict_[obj.page_name] = obj
#         for name, page in pages_dict_.items():
#             setattr(page, 'mapping', mappings_dict_[name])  # Injecting the mapping obj insede the page
#             setattr(self, name, page)  # Injecting the page obj
#             self._pages.append(page)
#
#     @property
#     def pages(self):
#         return self._pages
