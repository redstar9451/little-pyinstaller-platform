from abc import should_be_deleted
from abcd import do_not_be_deleted
from abc.ccc import should_be_deleted
from abcd.ccc import do_not_be_deleted

# should be deleted
import abc
import abc
import abc

# reserved
import abcd
