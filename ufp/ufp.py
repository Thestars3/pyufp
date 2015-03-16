#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from trashcli.trash import TrashPutCmd
import io

__all__ = ['trashPut']

def trashPut(target):
	"""
	@brief 대상을 휴지통에 버립니다.
	@details trashcli 패키지의 trash-put 명령어에 대한 인터페이스.
	
	@param taget 지울 대상의 경로 문자열
	
	@return True 성공시
	@return False 문제가 존재 할 시
	"""
	out = io.BytesIO()
	err = io.BytesIO()
	type(target)
	TrashPutCmd(out, err).run(['', '--', target.encode('utf8')])
	if err.getvalue():
		return False
	return True
