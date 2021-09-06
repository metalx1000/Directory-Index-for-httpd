# Directory-Index-for-httpd
Directory Index for Busybox's httpd

#Instructions
make sure cgi-bin is in your root server directory,
then run:

`busybox httpd -p 8000 -fv`


## Alternatives
* BusyBox have [httpd_indexcgi.c](https://github.com/mirror/busybox/blob/master/networking/httpd_indexcgi.c) which works without JS
* [busybox-httpd-directory-listing](https://github.com/HeGanjie/busybox-httpd-directory-listing) JS based
* [dir-index.cgi](https://gist.github.com/jow-/743363c332d09cb58a60dd1f216b6ee4) a Perl script
* [Making Our Own Indexes](https://docstore.mik.ua/orelly/linux/apache/ch07_02.htm) a tutorial how to make it yourself
