#include "led.h"
#include <stm32f10x.h>

void LED_init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure; //����ṹ��
	
	//ʱ���� -ʹ�ܶ�GPIOB��GPIOE�˿�ʱ��
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE); //LED0-PB5
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOE,ENABLE); //LED1-PB5
	
//	����GPIOB.5��GPIOE.5ģʽ
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; //�������
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	GPIO_SetBits(GPIOB,GPIO_Pin_5);//����PB5
	
	
}