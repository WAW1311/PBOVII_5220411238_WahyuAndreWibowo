class Universitas:
    def __init__(self,nama,lokasi):
        self.nama = nama
        self.lokasi = lokasi
        
    def informasi_univ(self):
        print(self.nama)
        print(self.lokasi)

class Pengajar(Universitas):
    def __init__(self,nama,jabatan,lokasi):
        super().__init__(nama,lokasi)
        self.__jabatan = jabatan
    
    def informasi_pengajar(self):
        print()
        self.informasi_univ()
        print(self.__jabatan)
        print()

class Dosen(Pengajar):
    def __init__(self,nama,jabatan,lokasi,prodi,matkul):
        super(Dosen,self).__init__(nama,jabatan,lokasi)
        self.__prodi = prodi
        self.__matkul = matkul
    
    def informasi_dosen(self):
        self.informasi_pengajar()
        print(self.__prodi)
        print(self.__matkul)

class Mahasiswa(Universitas):
    def __init__(self,npm,nama,fakultas,prodi,kelas,lokasi,ipk):
        super().__init__(nama,lokasi)
        self.__npm = npm
        self.fakultas = fakultas
        self.prodi = prodi
        self.__kelas = kelas
        self.__ipk = ipk
        self.__status = None
        
    def hitung_ipk(self, total = None):
        if total is not None:
            total_sks = 0
            total_nilai = 0
            for i in total:
                sks = i['sks']
                nilai = i['nilai']
                
                if nilai is not None:
                    total_sks += sks
                    total_nilai += sks * nilai
            
            if total_sks > 0:
                ipk = total_nilai / total_sks
                return ipk

        else:
            if self.__ipk >= 3.0:
                self.__status = "Lulus"
            else:
                self.__status = "Tidak lulus"
            
            
    def __informasi_mahasiswa(self):
        print(self.__npm)
        self.informasi_univ()
        print(self.fakultas)
        print(self.prodi)
        print(self.__kelas)
        print(self.__ipk)
        print(self.__status)

universitas = Universitas("Universitas Teknologi Yogyakarta","Yogyakarta")
pengajar = Pengajar('Tubagus Linux,S.KOM.,M.KOM.,Ph.D.',"Rektor","Yogyakarta")
dosen = Dosen('Arif Parameter,S.KOM.,M.KOM.','dosen','nganjuk','Informatika','pengembangan web')
mahasiswa = Mahasiswa(5220411123,"Ahmad Nginx","sains & teknologi","informatika","F","jepara",3.10)

universitas.informasi_univ()
pengajar.informasi_pengajar()
dosen.informasi_dosen()
print()
mahasiswa.hitung_ipk()
mahasiswa._Mahasiswa__informasi_mahasiswa()
print()
nilai = [{'sks': 3,'nilai':3.10},
         {'sks': 2,'nilai':3.20},
         {'sks': 1,'nilai':4.0},
         {'sks': 2,'nilai':3.50}]
print(mahasiswa.hitung_ipk(nilai))