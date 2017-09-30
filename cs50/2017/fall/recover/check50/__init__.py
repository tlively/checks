from check50 import *
import os

class Recover(Checks):
    hashes = [
        "af5d4d3920480f85d4c47be9fd538f5dfbf4937fd7f1153fa9aa2e5c96963707",  # 000.jpg
        "6996fb386f8f97d5352fad805d3adf0d4f2285bd7da7f0081050876b6f144974",  # 001.jpg
        "e7b2b4d3e7dcef5d3bc432ec899b7aca6486078dedaf5fd3b6a4861f1fe884c8",  # 002.jpg
        "91e9144adb34550447fe68ab6603db32a52bf7226eb7257132a55f0446f5d436",  # 003.jpg
        "ff14332d8916081d76895facf964e2605a8218973abee9ddfddf375630fa6464",  # 004.jpg
        "db66fdb0353e1a1cc72117d1fd2105aa85185533dd8f9255c949bb32b2151cfb",  # 005.jpg
        "64d38d7b239bb33b15e1f6c98759e455e68124b325dec581cc14d64efeeea2d3",  # 006.jpg
        "ea4190741a9ffc66fe1c54e17cbfed8f4faa9a16a3a328004aabe3f0a7e23758",  # 007.jpg
        "dbc61a1d664bb585f911eb4852c66f49e247865137b097a7718cc2c8a8ab48ea",  # 008.jpg
        "67a81febb0d0dbe5fd0a61f53fea1925c02be898855bda714dda3bc101ecff89",  # 009.jpg
        "775118ca83bac649d16c268fbf47c8950b72e9b0d8ce56cbc73c28f4797af9c6",  # 010.jpg
        "a0699810661598281d0788dc508b7c5c3e3cd8f45d293adbd96c0fce3bb7e06e",  # 011.jpg
        "0018682f939c81dc82f9a84368f433bc25feb4e09f160cce0facbf33b95e32ec",  # 012.jpg
        "d1dbd92fb666611b8d4419ee72e63f4ddb009f6e7807d4512ee3be4283030f21",  # 013.jpg
        "878066b209e4bcb97c806b410a7930c018bcdd32245014e43f664fb54d8374fb",  # 014.jpg
        "5e7213eb03f07db1b39cdc266f52727c7f8e7102d66191292619c473c9bdd393",  # 015.jpg
        "935b53246c28ca94ce90cd3d01e104d79e73797a9eeb4b16a6f930e6b535b461",  # 016.jpg
        "e5b740b53f3b0e410308128b4c5bfb2930da0ff11fa1a8386a0fbd15476bd131",  # 017.jpg
        "0bfd055454bca8798b4eff6dd0f57abc23c653a31d6d310104b82413596fece3",  # 018.jpg
        "4936141707bfae8d3d0080e0b16584dd65e260994727c8a8f33f1ffc242f433f",  # 019.jpg
        "3c5c37a5aa32386f527a060066f5812f37f6aef4d178191f1392e03db7f3fad0",  # 020.jpg
        "c596292224bf4e8b1cfc32a1649d1e0ee45cf563d35dffcc5d9819227efca992",  # 021.jpg
        "14ffd5ceede9a21bd18a50c7fe474f81a9c07fadba845ba21fb7d2ddaf87dca6",  # 022.jpg
        "7926d6654651964167561f9be2af5f417b1160598395f17d74e25540396b072e",  # 023.jpg
        "509f7233a90d1e50f0c01dc51c4f82df50ccb3e87b74801b414e36b3025219d5",  # 024.jpg
        "8ee5f5115b73aed853341c5cfe275d62d102de549c1cb1dd7aa2952ff9399c72",  # 025.jpg
        "9eba5b4bd473350f8a0ae2499782db240d97f995d0af16797f6356ac947eb7fb",  # 026.jpg
        "118d5bc8da0ee8e8b9eddddf94c76b2824c2d0eacc63b4da895446d301e288c6",  # 027.jpg
        "8c367af67f100fe7711f1aef2cd6540e39d55a058fb7c5d021346fb03df2093e",  # 028.jpg
        "0ac44b8fd5f2033f47789bd5508a6640145b00cda625a4e47ad687e8b26e49e5",  # 029.jpg
        "8401afea4b369a1162fba88e1ba575eeda9dbf8d32e89f65aba5e16a336af9e7",  # 030.jpg
        "374c2a1cb2059243d895fd5b4cca32a81b39d89560081695e700b1b5a09fd8d9",  # 031.jpg
        "d0bebb1d70b878c6d21fb93eddb249f953f025dfb1220fcf8859fc9c0af2e810",  # 032.jpg
        "c769f6b0671024cbe5cd6faffceb74394dfe008443a28f27c1b241f843062e0d",  # 033.jpg
        "2ed1081072bf80ce9ad70b32a14dbfd7f3a1d9b44d5bf4ad8afecceaa0b339fd",  # 034.jpg
        "22aa5c24c5ad996e90206ce6ae30831664b72da54913f3f605b230fb38c8ba72",  # 035.jpg
        "c1fbf91e81d6415173877b1e46eb1c42ac42ceef3f8ff25ce6df5513aed857e2",  # 036.jpg
        "ae9c3a8edb9cffda2851dab19aa9cf6a739e4d8de73759c503c86e224724d32f",  # 037.jpg
        "6b50f8c8347a3812f1544850cbb58add8a89832f7e5d38984ef9c4b9abcd15ec",  # 038.jpg
        "716209360e14e560d7a699b20fc995da2834f34b887c42e60abbf7042dd600b2",  # 039.jpg
        "5a5845a83b0c87a5d55d283cc72404e225ab6fb17a8ccb17e6c67aff3a615c58",  # 040.jpg
        "cadd73e00adf817b1d28a7c13b5e7de380f8694076627274d1e065a75d13f1fe",  # 041.jpg
        "6ed99c19c816b4185698f53f269ef49962266a3a304da0f76817e49f158ad8e1",  # 042.jpg
        "67c274202baa4be7014cb7c37d320a6c2d36a427df4b4fe0dd6142cc0ac16beb",  # 043.jpg
        "e979434108eb0ff671b994fce7ea8aeed0b279c3676bf3e55b71cc053856e1b5",  # 044.jpg
        "0e98bb0e05a369af19f3e7da424e0ba71e03e0ade261b891658d0c55f6f8bd7d",  # 045.jpg
        "f453159b15fece6328baf7896566a9c70aa0fa6ddacc1bdbbdff6e1d07acab8e",  # 046.jpg
        "a54365a22e0cac5999afcfb3c1f2ab6cfd431cad7c1d3e1396a8de82677f7e07",  # 047.jpg
        "c00d1cc7eb5c31b9ae2acafb7c0e27960c215c8b5558f6a8057490266f3a0646",  # 048.jpg
        "3510482b20a5b93eb8e8558227fa80f8460581f71e433932d11bac989e9d17fc"   # 049.jpg
    ]

    sizes = [
        45568,   # 000.jpg
        51200,   # 001.jpg
        20992,   # 002.jpg
        26112,   # 003.jpg
        62976,   # 004.jpg
        221696,  # 005.jpg
        183296,  # 006.jpg
        54784,   # 007.jpg
        45568,   # 008.jpg
        171520,  # 009.jpg
        35840,   # 010.jpg
        57856,   # 011.jpg
        173056,  # 012.jpg
        75776,   # 013.jpg
        49152,   # 014.jpg
        202752,  # 015.jpg
        22016,   # 016.jpg
        183296,  # 017.jpg
        31232,   # 018.jpg
        44032,   # 019.jpg
        194560,  # 020.jpg
        56832,   # 021.jpg
        220672,  # 022.jpg
        77824,   # 023.jpg
        25088,   # 024.jpg
        233984,  # 025.jpg
        235008,  # 026.jpg
        32768,   # 027.jpg
        44032,   # 028.jpg
        208896,  # 029.jpg
        39936,   # 030.jpg
        49664,   # 031.jpg
        278528,  # 032.jpg
        221696,  # 033.jpg
        47616,   # 034.jpg
        179712,  # 035.jpg
        20480,   # 036.jpg
        55808,   # 037.jpg
        202240,  # 038.jpg
        86528,   # 039.jpg
        56832,   # 040.jpg
        226304,  # 041.jpg
        210432,  # 042.jpg
        161792,  # 043.jpg
        21504,   # 044.jpg
        60928,   # 045.jpg
        16896,   # 046.jpg
        27648,   # 047.jpg
        162304,  # 048.jpg
        34304    # 049.jpg
    ]

    @check()
    def exists(self):
        """recover.c exists."""
        self.require("recover.c")

    @check("exists")
    def compiles(self):
        """recover.c compiles."""
        self.spawn("clang -std=c11 -o recover recover.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_noimage(self):
        """handles lack of forensic image"""
        self.spawn("./recover").exit(1)

    @check("compiles")
    def first_image(self):
        """recovers 000.jpg correctly"""
        self.add("card.raw")
        self.spawn("./recover card.raw").exit(0, timeout=10)
        self.check_jpg(0)

    @check("compiles")
    def middle_images(self):
        """recovers middle images correctly"""
        self.add("card.raw")
        self.spawn("./recover card.raw").exit(0, timeout=10)
        for i in range(49):
            self.check_jpg(i)

    @check("compiles")
    def last_image(self):
        """recovers 049.jpg correctly"""
        self.add("card.raw")
        self.spawn("./recover card.raw").exit(0, timeout=10)
        self.check_jpg(49)

    def check_jpg(self, i):
        jpg = "{:03d}.jpg".format(i)
        self.require(jpg)

        if self.hash(jpg) == self.hashes[i]:
            return

        err = Error("recovered image does not match")

        with open(jpg, "rb") as f:
            header = bytearray(f.read(4))
        if len(header) >= 4:
            header[3] = header[3] & 0xf0

        file_len = os.path.getsize(jpg)

        if header != b'\xff\xd8\xff\xf0':
            err.helpers = "Does {} have a correct jpeg header?".format(jpg)
        elif file_len % 512 != 0:
            err.helpers = "Is {} a multiple of 512 bytes?".format(jpg)
        elif file_len < self.sizes[i]:
            err.helpers = "It looks like {} is shorter than expected.".format(jpg)
        elif file_len > self.sizes[i]:
            err.helpers = "It looks like {} is longer than expected.".format(jpg)
        raise err
