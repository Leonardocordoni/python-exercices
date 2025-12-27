import mailbox
import email.utils
import email.header
import csv
import json
from datetime import datetime
from openpyxl import Workbook

# ===== CONFIGURAÇÃO =====
# Coloque aqui o caminho do seu arquivo MBOX
MBOX_FILE = "Todos os e-mails, incluindo Spam e Lixeira.mbox"  # ou o nome do seu arquivo

# Nomes dos arquivos de saída
CSV_FILE = "emails.csv"
XLSX_FILE = "emails.xlsx"
JSON_FILE = "emails.json"

# ========================

def parse_date(date_str):
    """Converte a data do e-mail para formato legível"""
    if not date_str:
        return "Data desconhecida"
    try:
        parsed = email.utils.parsedate_to_datetime(date_str)
        return parsed.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return date_str

def decode_header_field(field):
    """Decodifica campos do cabeçalho (assunto, remetente, etc.)"""
    if not field:
        return ""
    
    decoded_parts = []
    for part, encoding in email.header.decode_header(field):
        if isinstance(part, bytes):
            # Tenta decodificar com a codificação especificada ou UTF-8
            try:
                decoded_parts.append(part.decode(encoding or 'utf-8', errors='replace'))
            except:
                decoded_parts.append(part.decode('utf-8', errors='replace'))
        else:
            decoded_parts.append(str(part))
    
    result = ''.join(decoded_parts)
    # Remove quebras de linha
    result = result.replace('\n', ' ').replace('\r', ' ')
    return result.strip()

def extract_emails(mbox_path):
    """Extrai data, assunto e remetente de todos os e-mails"""
    print(f"📧 Lendo arquivo MBOX: {mbox_path}")
    print("⏳ Isso pode demorar alguns minutos dependendo do tamanho...\n")
    
    mbox = mailbox.mbox(mbox_path)
    emails_data = []
    count = 0
    
    for message in mbox:
        count += 1
        if count % 1000 == 0:
            print(f"   Processados {count} e-mails...")
        
        # Extrai os campos
        date_received = parse_date(message.get("Date"))
        subject_raw = message.get("Subject", "(Sem assunto)")
        sender_raw = message.get("From", "(Remetente desconhecido)")
        
        # Decodifica os campos
        subject = decode_header_field(subject_raw)
        sender = decode_header_field(sender_raw)
        
        # Se ficou vazio após decodificação
        if not subject:
            subject = "(Sem assunto)"
        if not sender:
            sender = "(Remetente desconhecido)"
        
        emails_data.append({
            "data_recebimento": date_received,
            "assunto": subject,
            "remetente": sender
        })
    
    print(f"\n✅ Total de e-mails processados: {count}\n")
    return emails_data

def save_to_csv(data, filename):
    """Salva os dados em CSV"""
    print(f"💾 Salvando CSV: {filename}")
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=["data_recebimento", "assunto", "remetente"])
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ CSV salvo com sucesso!\n")

def save_to_xlsx(data, filename):
    """Salva os dados em Excel"""
    print(f"💾 Salvando Excel: {filename}")
    wb = Workbook()
    ws = wb.active
    ws.title = "Emails"
    
    # Cabeçalhos
    ws.append(["Data de Recebimento", "Assunto", "Remetente"])
    
    # Dados
    for item in data:
        ws.append([item["data_recebimento"], item["assunto"], item["remetente"]])
    
    # Ajusta largura das colunas
    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 40
    
    wb.save(filename)
    print(f"✅ Excel salvo com sucesso!\n")

def save_to_json(data, filename):
    """Salva os dados em JSON"""
    print(f"💾 Salvando JSON: {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON salvo com sucesso!\n")

# ===== EXECUÇÃO PRINCIPAL =====
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 EXTRATOR DE E-MAILS DO MBOX")
    print("=" * 60 + "\n")
    
    # Extrai os dados
    emails = extract_emails(MBOX_FILE)
    
    if not emails:
        print("❌ Nenhum e-mail encontrado no arquivo MBOX.")
        exit()
    
    # Salva nos 3 formatos
    save_to_csv(emails, CSV_FILE)
    save_to_xlsx(emails, XLSX_FILE)
    save_to_json(emails, JSON_FILE)
    
    print("=" * 60)
    print("🎉 CONCLUÍDO!")
    print("=" * 60)
    print(f"\n📂 Arquivos gerados:")
    print(f"   • {CSV_FILE}")
    print(f"   • {XLSX_FILE}")
    print(f"   • {JSON_FILE}")
    print(f"\n📊 Total de e-mails: {len(emails)}")