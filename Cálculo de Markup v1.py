# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:36:20 2024

@author: Silas Carvalho

This code is released under the MIT License.

Copyright (c) 2024 Silas Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from colorama import Fore, Style, init
from decimal import Decimal, getcontext, ROUND_HALF_UP, InvalidOperation

init(autoreset=True)
getcontext().prec = 10

def round_decimal(value):
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def input_decimal(mensagem):
    while True:
        try:
            valor_str = input(mensagem).replace(',', '.')
            valor = Decimal(valor_str)
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except (ValueError, InvalidOperation) as e:
            print(f"{Fore.RED}Por favor, insira um número válido. Erro: {e}")

def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                raise ValueError("O número não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"{Fore.RED}Por favor, insira um número inteiro válido. Erro: {e}")

def input_s_n(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print(f"{Fore.RED}Por favor, digite 's' para sim ou 'n'.")

def print_section(title):
    length = len(title) + 8
    line = f"{Fore.YELLOW}{'=' * length}{Style.RESET_ALL}"
    print(f"\n{line}")
    print(f"   {title}")
    print(line)

def calcular_precos():
    while True:
        print_section("CÁLCULO DE MARKUP")
        preco_compra = input_decimal("Digite o preço de compra: R$ ")

        adicionar_custos_extras = input_s_n("Deseja adicionar custos extras? (s/n): ")
        custos_extras = Decimal('0.00')
        if adicionar_custos_extras == 's':
            num_custos_extras = input_int("Quantos custos extras deseja adicionar? ")
            for i in range(num_custos_extras):
                nome_custo = input(f"Digite o nome do custo extra {i+1}: ")
                valor_custo = input_decimal(f"Digite o valor do {nome_custo}: R$ ")
                custos_extras += valor_custo

            total_com_extras = preco_compra + custos_extras
            print(f"\nTotal dos Custos Extras: R$ {custos_extras:.2f}")
            print(f"Total (Compra + Custos Extras): R$ {total_com_extras:.2f}")
        else:
            total_com_extras = preco_compra

        print_section("CONFIGURAÇÕES DE GANHO ESTIMADO")
        ganho_estimado_percent = input_decimal("Digite o ganho estimado (% para markup): ")
        markup_percent = ganho_estimado_percent + Decimal('100.00')

        preco_custo_total = total_com_extras
        preco_venda = round_decimal(preco_custo_total * (markup_percent / 100))

        lucro_bruto = round_decimal(preco_venda - preco_custo_total)
        margem = round_decimal((lucro_bruto / preco_venda) * 100)

        print_section("RESULTADOS DO CÁLCULO DE MARKUP")
        print(f"Preço de Custo Total: R$ {preco_custo_total:.2f}")
        print(f"Preço de Venda: R$ {preco_venda:.2f}")
        print(f"Lucro Bruto: R$ {lucro_bruto:.2f}")
        print(f"{Fore.LIGHTBLUE_EX}Ganho estimado (baseado no markup inicial): {ganho_estimado_percent:.1f}%{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}Margem de Lucro (calculada com o preço de venda inicial): {margem:.2f}%{Style.RESET_ALL}")

        incluir_taxa_cartao_markup = input_s_n("\nDeseja incluir a taxa de cartão para o markup? (s/n): ")
        if incluir_taxa_cartao_markup == 's':
            taxa_cartao_percent_markup = input_decimal("Digite a taxa de cartão (%): ")
            while taxa_cartao_percent_markup > 100 or taxa_cartao_percent_markup < 0:
                print("Por favor, insira um percentual válido entre 0 e 100.")
                taxa_cartao_percent_markup = input_decimal("Digite a taxa de cartão (%): ")
            valor_taxa_cartao_markup = round_decimal(preco_venda * (taxa_cartao_percent_markup / 100))
            preco_ideal_sugerido_markup = round_decimal(preco_venda + valor_taxa_cartao_markup)

            print_section("PREÇO IDEAL SUGERIDO (MARKUP)")
            print(f"Taxas de cartão: {taxa_cartao_percent_markup}% \tR$ {valor_taxa_cartao_markup:.2f}")
            print(f"Preço com Tx de cartão: R$ {preco_ideal_sugerido_markup:.2f}")

        calcular_margem = input_s_n("\nDeseja calcular a margem de lucro com outro preço de venda? (s/n): ")
        if calcular_margem == 's':
            preco_venda_usuario = input_decimal("Digite o preço de venda desejado: R$ ")
            lucro_bruto_usuario = round_decimal(preco_venda_usuario - preco_custo_total)
            margem_usuario = round_decimal((lucro_bruto_usuario / preco_venda_usuario) * 100)
            print_section("MARGEM DE LUCRO (Preço de Venda Alternativo)")
            print(f"Preço de Venda Desejado: R$ {preco_venda_usuario:.2f}")
            print(f"Lucro Bruto: R$ {lucro_bruto_usuario:.2f}")
            print(f"{Fore.LIGHTYELLOW_EX}Margem de Lucro (calculada com o preço de venda alternativo): {margem_usuario:.2f}%{Style.RESET_ALL}")

            incluir_taxa_cartao_margem = input_s_n("\nDeseja incluir a taxa de cartão para a margem? (s/n): ")
            if incluir_taxa_cartao_margem == 's':
                taxa_cartao_percent_margem = input_decimal("Digite a taxa de cartão (%): ")
                while taxa_cartao_percent_margem > 100 or taxa_cartao_percent_margem < 0:
                    print("Por favor, insira um percentual válido entre 0 e 100.")
                    taxa_cartao_percent_margem = input_decimal("Digite a taxa de cartão (%): ")
                valor_taxa_cartao_margem = round_decimal(preco_venda_usuario * (taxa_cartao_percent_margem / 100))
                preco_ideal_sugerido_margem = round_decimal(preco_venda_usuario + valor_taxa_cartao_margem)

                print_section("PREÇO IDEAL SUGERIDO (MARGEM)")
                print(f"Taxas de cartão: {taxa_cartao_percent_margem}% \tR$ {valor_taxa_cartao_margem:.2f}")
                print(f"Preço com Tx de cartão: R$ {preco_ideal_sugerido_margem:.2f}")

        print_section("COMPARAÇÃO FINAL")
        print(f"Preço de Venda (Markup): R$ {preco_venda:.2f}")
        print(f"Preço de Venda (Margem): R$ {preco_venda_usuario:.2f}")
        print(f"Lucro Bruto (Markup): R$ {lucro_bruto:.2f}")
        print(f"Lucro Bruto (Margem): R$ {lucro_bruto_usuario:.2f}")
        print(f"{Fore.LIGHTGREEN_EX}Margem de Lucro (calculada com o preço de venda inicial): {margem:.2f}%{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Margem de Lucro (Preço de Venda Alternativo): {margem_usuario:.2f}%{Style.RESET_ALL}")

        repetir = input_s_n("\nDeseja fazer outro cálculo? (s/n): ")
        if repetir != 's':
            print("Encerrando o programa. Obrigado!")
            break

calcular_precos()

