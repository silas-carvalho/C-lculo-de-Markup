# Cálculo de Markup v1

O projeto "Cálculo de Markup v1" está em desenvolvimento e visa oferecer uma ferramenta robusta e amigável para calcular markup e diferenciar entre o ganho estimado e o ganho realizado.

## Pré-requisitos

Certifique-se de que você tem o Python 3.x instalado em seu sistema. O Python 3.x pode ser encontrado na Microsoft Store.

## Instalar dependências

Windows Power Shell
```bash
pip install colorama
```

Linux ou MacOs
```bash
sudo pip install colorama
```

# Fórmulas

Fórmula de markup escolhida para utilizar na programação
```bash
PV = CUSTO * (1 + MARKUP% / 100)
```

Parte do código onde a fórmula de markup escolhida foi aplicada
```bash
preco_custo_total = preco_compra + custos_extras
markup_percent = input_float("Digite o markup desejado (%): ")
preco_venda = preco_custo_total * (1 + markup_percent / 100)
```

Fórmula de margem escolhida para utilizar na programação
```bash
Margem = (lucro bruto / preço de venda) x 100
```

Parte do código onde a fórmula de margem escolhida foi aplicada
```bash
lucro_bruto = preco_venda - preco_custo_total
margem = (lucro_bruto / preco_venda) * 100
```


