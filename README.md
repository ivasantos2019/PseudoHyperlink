# 🔗 PseudoHyperlink – Plugin para QGIS

**PseudoHyperlink** é um plugin para QGIS que permite criar **links clicáveis em dicas HTML (pop-ups)** associadas a feições em camadas vetoriais. Isso permite ações como:

- 🔍 Zoom automático em feições específicas
- 🌐 Abertura de links externos (páginas da web)
- 📄 Acesso direto a documentos locais (PDF, DOC, etc.)

---

## ⚙️ Funcionalidades

- Suporte a links do tipo `qgis://zoom?id=123`
- Abertura de arquivos com `file:///caminho/para/arquivo.pdf`
- Totalmente integrado com dicas HTML do QGIS
- Útil para projetos interativos de gestão florestal, urbana, agrícola e mais

---

## 🛠️ Requisitos

- QGIS 3.16 ou superior (recomendado: QGIS 3.34+)
- Sistema com navegador e/ou visualizador de arquivos padrão

---

## 📦 Instalação

1. Baixe ou clone este repositório
2. Compacte a pasta em um arquivo `.zip`
3. No QGIS, acesse **Complementos > Gerenciar e Instalar Complementos > Instalar a partir de um arquivo ZIP**
4. Selecione o arquivo `.zip` e instale

---

## 💡 Exemplo de uso

Adicione a seguinte dica HTML em uma camada de pontos:

```html
<a href="qgis://zoom?id=10">Clique para fazer zoom</a>

