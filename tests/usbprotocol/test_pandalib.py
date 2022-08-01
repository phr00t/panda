#!/usr/bin/env python3
import random
import unittest
from panda import pack_can_buffer, unpack_can_buffer, DLC_TO_LEN


class PandaTestPackUnpack(unittest.TestCase):
  def test_panda_lib_pack_unpack(self):
    to_pack = []
    for _ in range(10000):
      address = random.randint(1, 0x1FFFFFFF)
      data = bytes([random.getrandbits(8) for _ in range(DLC_TO_LEN[random.randrange(len(DLC_TO_LEN))])])
      print(len(data))
      to_pack.append((address, 0, data, 0))

    packed = pack_can_buffer(to_pack)
    unpacked = []
    
    counter = None
    for dat in packed:
      msgs, counter = unpack_can_buffer(dat, prev_rx_counter=counter)
      unpacked.extend(msgs)

    assert unpacked == to_pack

if __name__ == "__main__":
  unittest.main()
