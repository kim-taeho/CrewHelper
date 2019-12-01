# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "남성"),
        (GENDER_FEMALE, "여성"),
    )

    MAJOR_1 = "글로벌지역학"
    MAJOR_2 = "EU전공"
    MAJOR_3 = "GlobalBusiness"
    MAJOR_4 = "TESOL영어학전공"
    MAJOR_5 = "광고PR브랜딩전공"
    MAJOR_6 = "교육학"
    MAJOR_7 = "국가리더전공"
    MAJOR_8 = "국제금융학과"
    MAJOR_9 = "국제스포츠레저전공"
    MAJOR_10 = "그리스불가리아학과"
    MAJOR_11 = "남아프리카어전공"
    MAJOR_12 = "독일어통번역학과"
    MAJOR_13 = "동아프리카어전공"
    MAJOR_14 = "동유럽학대학"
    MAJOR_15 = "러시아학과"
    MAJOR_16 = "루마니아어과"
    MAJOR_17 = "말레이인도네시아어통번역학과"
    MAJOR_18 = "문화콘텐츠학전공"
    MAJOR_19 = "바이오메디컬공학전공"
    MAJOR_20 = "방송영상뉴미디어전공"
    MAJOR_21 = "브라질학과"
    MAJOR_22 = "사학과"
    MAJOR_23 = "산업경영공학과"
    MAJOR_24 = "생명공학과"
    MAJOR_25 = "서아프리카어전공"
    MAJOR_26 = "세계문화예술경영전공"
    MAJOR_27 = "세르비아크로아티아어과"
    MAJOR_28 = "수학과"
    MAJOR_29 = "스페인어통번역학과"
    MAJOR_30 = "아랍어통번역학과"
    MAJOR_31 = "아프리카학부"
    MAJOR_32 = "언론정보전공"
    MAJOR_33 = "언어인지과학과"
    MAJOR_34 = "영미권통상통번역전공"
    MAJOR_35 = "영미문학번역전공"
    MAJOR_36 = "영어통번역학부"
    MAJOR_37 = "영어통번역학전공"
    MAJOR_38 = "우크라이나어과"
    MAJOR_39 = "융복합소프트웨어전공"
    MAJOR_40 = "이탈리아어통번역학과"
    MAJOR_41 = "인도학과"
    MAJOR_42 = "일본어통번역학과"
    MAJOR_43 = "전자공학과"
    MAJOR_44 = "전자물리학과"
    MAJOR_45 = "정보기록학전공"
    MAJOR_46 = "정보통신공학과"
    MAJOR_47 = "정치외교학과"
    MAJOR_48 = "중국어통번역학과"
    MAJOR_49 = "중앙아시아학과"
    MAJOR_50 = "지식콘텐츠전공"
    MAJOR_51 = "철학과"
    MAJOR_52 = "체코슬로바키아어과"
    MAJOR_53 = "컴퓨터전자시스템공학전공"
    MAJOR_54 = "태국어통번역학과"
    MAJOR_55 = "통계학과"
    MAJOR_56 = "폴란드어과"
    MAJOR_57 = "프랑스학과"
    MAJOR_58 = "한국학과"
    MAJOR_59 = "행정학과"
    MAJOR_60 = "헝가리어과"
    MAJOR_61 = "화학과"
    MAJOR_62 = "환경학과"

    MAJOR_CHOICES = (
        (MAJOR_1, "글로벌지역학"),
        (MAJOR_2, "EU전공"),
        (MAJOR_3, "GlobalBusiness"),
        (MAJOR_4, "TESOL영어학전공"),
        (MAJOR_5, "광고PR브랜딩전공"),
        (MAJOR_6, "교육학"),
        (MAJOR_7, "국가리더전공"),
        (MAJOR_8, "국제금융학과"),
        (MAJOR_9, "국제스포츠레저전공"),
        (MAJOR_10, "그리스불가리아학과"),
        (MAJOR_11, "남아프리카어전공"),
        (MAJOR_12, "독일어통번역학과"),
        (MAJOR_13, "동아프리카어전공"),
        (MAJOR_14, "동유럽학대학"),
        (MAJOR_15, "러시아학과"),
        (MAJOR_16, "루마니아어과"),
        (MAJOR_17, "말레이인도네시아어통번역학과"),
        (MAJOR_18, "문화콘텐츠학전공"),
        (MAJOR_19, "바이오메디컬공학전공"),
        (MAJOR_20, "방송영상뉴미디어전공"),
        (MAJOR_21, "브라질학과"),
        (MAJOR_22, "사학과"),
        (MAJOR_23, "산업경영공학과"),
        (MAJOR_24, "생명공학과"),
        (MAJOR_25, "서아프리카어전공"),
        (MAJOR_26, "세계문화예술경영전공"),
        (MAJOR_27, "세르비아크로아티아어과"),
        (MAJOR_28, "수학과"),
        (MAJOR_29, "스페인어통번역학과"),
        (MAJOR_30, "아랍어통번역학과"),
        (MAJOR_31, "아프리카학부"),
        (MAJOR_32, "언론정보전공"),
        (MAJOR_33, "언어인지과학과"),
        (MAJOR_34, "영미권통상통번역전공"),
        (MAJOR_35, "영미문학번역전공"),
        (MAJOR_36, "영어통번역학부"),
        (MAJOR_37, "영어통번역학전공"),
        (MAJOR_38, "우크라이나어과"),
        (MAJOR_39, "융복합소프트웨어전공"),
        (MAJOR_40, "이탈리아어통번역학과"),
        (MAJOR_41, "인도학과"),
        (MAJOR_42, "일본어통번역학과"),
        (MAJOR_43, "전자공학과"),
        (MAJOR_44, "전자물리학과"),
        (MAJOR_45, "정보기록학전공"),
        (MAJOR_46, "정보통신공학과"),
        (MAJOR_47, "정치외교학과"),
        (MAJOR_48, "중국어통번역학과"),
        (MAJOR_49, "중앙아시아학과"),
        (MAJOR_50, "지식콘텐츠전공"),
        (MAJOR_51, "철학과"),
        (MAJOR_52, "체코슬로바키아어과"),
        (MAJOR_53, "컴퓨터전자시스템공학전공"),
        (MAJOR_54, "태국어통번역학과"),
        (MAJOR_55, "통계학과"),
        (MAJOR_56, "폴란드어과"),
        (MAJOR_57, "프랑스학과"),
        (MAJOR_58, "한국학과"),
        (MAJOR_59, "행정학과"),
        (MAJOR_60, "헝가리어과"),
        (MAJOR_61, "화학과"),
        (MAJOR_62, "환경학과"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "EMAIL"),
        (LOGIN_KAKAO, "KAKAO"),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="")
    major = models.CharField(choices=MAJOR_CHOICES, max_length=20, blank=True)
    login_method = models.CharField(
        choices=LOGIN_CHOICES, max_length=50, default=LOGIN_EMAIL
    )

    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

