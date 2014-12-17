# coding: utf-8

from StringIO import StringIO
from nose.tools import with_setup

import leancloud
from leancloud import File
from leancloud import ACL

__author__ = 'asaka'


def setup_func():
    leancloud.init(
        'pgk9e8orv8l9coak1rjht1avt2f4o9kptb0au0by5vbk9upb',
        'hi4jsm62kok2qz2w2qphzryo564rzsrucl2czb0hn6ogwwnd',
    )


def test_basic():
    s = StringIO('blah blah blah')
    f = File('blah', s)
    assert f.name == 'blah'
    assert f._metadata['size'] == 14
    assert f._type == 'text/plain'


def test_create_with_url():
    f = File.create_with_url('xxx', 'http://www.leancloud.cn')
    assert f.url == 'http://www.leancloud.cn'


def test_create_without_data():
    f = File.create_without_data(123)
    assert f.id == 123


def test_acl():
    acl = ACL()
    f = File('blah', buffer('xxx'))
    f.set_acl(acl)
    assert f.get_acl() == acl


@with_setup(setup_func)
def test_save():
    f = File('blah', buffer('xxx'))
    f.save()


@with_setup(setup_func)
def test_save_external():
    f = File.create_with_url('lenna.jpg', 'http://www.lenna.org/full/len_std.jpg')
    f.save()
