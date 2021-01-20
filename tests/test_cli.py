# MIT License

# Copyright (c) 2021 Rene Jean Corneille

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import datetime
import pytest

from package_name.cli import _get_str_date

@pytest.mark.parametrize(
    "date, fmt, result",
    [
       (datetime.datetime(2018, 10, 18, 14, 30, 59), '%Y-%B-%d, %H:%M:%S', '2018-October-18, 14:30:59'),
       (datetime.datetime(2025, 9, 1, 4, 16, 22), '%y-%m-%d, %H:%M:%S', '25-09-01, 04:16:22'),
       (datetime.datetime(1987, 3, 25, 21, 11, 2), '%Y-%B-%d', '1987-March-25'),
    ],
)
def test_format_date(date, fmt, result):
    """Test get str date fn."""
    assert _get_str_date(date, fmt) == result