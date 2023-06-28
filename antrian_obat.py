class Queue:
    def __init__(self,n=30):
        self.size= n
        self.current_size= 0
        self.data= []
    
    def isFull(self):
        if self.current_size == self.size:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.current_size == 0:
            return True
        else:
            return False
        
    def enqueue(self,n):
        if self.isFull():
            print('Mohon maaf antrian sudah penuh')
        else:
            self.data.append(n)
            self.current_size= len(self.data)
            print('Antrian dengan nama',n,'telah ditambahkan')
        print('Tekan [enter] untuk melanjutkan')
        input()
        self.menu()
    
    def dequeue(self):
        if self.isEmpty():
            print('Maaf antrian pengambilan obat masih kosong')
            return None
        else:
            datakeluar= self.data.pop(0)
            self.current_size= len(self.data)
            print('--------------------')
            print('Antrian dengan nama: ', datakeluar)
            print('Mohon untuk mengambil obat')
            print('--------------------')
            print('Antrian setelah ini adalah:', self.data)
            print('Tekan [enter] untuk melanjutkan')
            input()
            self.menu()

    def view(self):
        if self.isEmpty():
            print('Mohon maaf antrian masih kosong')
        else:
            print('========== DAFTAR ANTRIAN ==========')

            x= 1
            for i in self.data:
                print('',str(x)+'. ',i)
                x+= 1
            print('Total antrian: ',len(self.data))
        print('Tekan [enter] untuk melanjutkan')
        input()
        self.menu()

    def Exit(self):
        print('Anda telah keluar')
        import sys
        sys.exit()

    def menu(self):
        print('===============================')
        print('|PROGRAM ANTRIAN|')
        print('|APOTEK INF|')
        print('|Daftar Menu|')
        print('1. Tambah Antrian')
        print('2. Panggil Antrian')
        print('3. Daftar Antrian')
        print('4. Keluar')
        print('===============================')

        pil= int(input('Masukkan nomor menu yang ingin dipilih: '))
        if pil == 1:
            data= input('Masukan nama: ')
            self.enqueue(data)
        elif pil == 2:
            self.dequeue()
        elif pil == 3:
            self.view()
        elif pil == 4:
            self.Exit
        else:
            print('Mohon maaf pilihan yang anda masukkan salah')
            print('Tekan [enter] untuk kembali ke Menu')
            input()

            self.menu()

q= Queue()
q.menu()
