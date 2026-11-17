from netmiko import ConnectHandler

# Paramètres de connexion de votre Catalyst 9000 Sandbox
cisco_switch = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec9k.cisco.com",
    "username": "20ib059",
    "password": "#i1kHTerLe!8_5",
}

try:
    print("Connexion au routeur/commutateur en cours via Netmiko...")
    with ConnectHandler(**cisco_switch) as net_connect:
        print("Connexion établie avec succès !\n" + "="*50)

        # 1. Afficher le nom du routeur, sa version du OS et le modèle
        print("--- 1. INFORMATIONS GENERALES (show version) ---")
        print(net_connect.send_command("show version"))
        print("="*50)

        # 2, 3 & 4. Interfaces Up / Down et comptage des types de ports
        print("--- 2, 3 & 4. ANALYSE DES INTERFACES (show ip interface brief) ---")
        output_brief = net_connect.send_command("show ip interface brief")
        print(output_brief)

        fa_count = 0
        gig_count = 0
        for line in output_brief.splitlines():
            if "FastEthernet" in line or "Fa" in line:
                fa_count += 1
            elif "GigabitEthernet" in line or "Gi" in line or "TenGigabitEthernet" in line:
                gig_count += 1

        print(f"\n[Statistiques] Ports FastEthernet : {fa_count} | Ports Gigabit/TenGigabit : {gig_count}")
        print("="*50)

        # 5. Afficher la liste des réseaux accessibles via le routeur
        print("--- 5. RESEAUX ACCESSIBLES (show ip route) ---")
        print(net_connect.send_command("show ip route"))
        print("="*50)

except Exception as e:
    print(f"Une erreur est survenue lors de la connexion : {e}")
