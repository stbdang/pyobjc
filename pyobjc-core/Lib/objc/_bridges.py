import collections.abc
import datetime

from objc import _objc

__all__ = [
    "registerListType",
    "registerMappingType",
    "registerSetType",
    "registerDateType",
]


def registerListType(type):
    """
    Register 'type' as a list-like type that will be proxied
    as an NSMutableArray subclass.
    """
    if _objc.options._sequence_types is None:
        _objc.options._sequence_types = ()

    _objc.options._sequence_types += (type,)


def registerMappingType(type):
    """
    Register 'type' as a dictionary-like type that will be proxied
    as an NSMutableDictionary subclass.
    """
    if _objc.options._mapping_types is None:
        _objc.options._mapping_types = ()

    _objc.options._mapping_types += (type,)


def registerSetType(type):
    """
    Register 'type' as a set-like type that will be proxied
    as an NSMutableSet subclass.
    """
    if _objc.options._set_types is None:
        _objc.options._set_types = ()

    _objc.options._set_types += (type,)


def registerDateType(type):
    """
    Register 'type' as a date-like type that will be proxied
    as an NSDate subclass.
    """
    if _objc.options._date_types is None:
        _objc.options._date_types = ()

    _objc.options._date_types += (type,)


registerListType(collections.abc.Sequence)
registerListType(range)
registerMappingType(collections.abc.Mapping)
registerMappingType(dict)
registerSetType(set)
registerSetType(frozenset)
registerSetType(collections.abc.Set)
registerDateType(datetime.date)
registerDateType(datetime.datetime)
