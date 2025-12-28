# Clean Makefile for MFEM serial build
MFEM_DIR = <.....path to.......>/mfem-<x.y>
CXX = g++
CXXFLAGS = -std=c++11 -I$(MFEM_DIR)
LDFLAGS = $(MFEM_DIR)/libmfem.a
TARGET =<.... problem name ....>
SRC = <....problem...>.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
