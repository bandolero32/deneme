#!/usr/bin/ env python
# -*- coding: utf-8 -*-
import hashlib
key_string = raw_input( "Şifre giriniz : " ) 
print hashlib.md5( key_string ).hexdigest()
