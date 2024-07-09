library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity ram is
    Port ( clk_in : in STD_LOGIC;
           reset : in STD_LOGIC;
           enable_in : in STD_LOGIC;
           write_enable_in : in STD_LOGIC;
           address_in : in STD_LOGIC_VECTOR (15 downto 0);
           data_in : in STD_LOGIC_VECTOR (15 downto 0);
           data_out : out STD_LOGIC_VECTOR (15 downto 0));
end ram;

architecture Behavioral of ram is
    type ram_array is array (0 to 255) of STD_LOGIC_VECTOR (15 downto 0); -- 256 addresses of 16 bits = 512B memory
    --signal ram: ram_array := (others => x"0000");
    signal ram: ram_array := (   
		"1000000101001100",
		"1000100000110000",
		"0000000110011100",
		"0010110101100100",
		
        others => x"0000"
    );
    
begin
    process(clk_in)
    begin
        if rising_edge(clk_in) then
            --if(reset = '1') then
            --    ram <= (others => x"0000");
            --end if;
            if(write_enable_in = '1') then
                ram(to_integer(unsigned(address_in(7 downto 0)))) <= data_in; -- 2^8 = 256
            else
                data_out <= ram(to_integer(unsigned(address_in(7 downto 0))));
            end if;
        end if;
     end process;

end Behavioral;