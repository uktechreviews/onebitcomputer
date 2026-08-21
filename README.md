# one bit computer

<br> My own interpretation of the one bit computer based on the Usagi Electric YouTube channel [^1]

<br>

<img width="571" height="428" alt="Development" src="https://github.com/user-attachments/assets/cdf5c670-4923-4ad9-a5b2-a212902e2877" />

<br>

### Main build task list

<br>

- [x] Automatic clock with variable speed
- [x] Manual clock progression with debounce
- [x] Program counter (max 8 bits) 
- [x] Pause clock
- [x] Reset clock
- [x] Binary LED display of program counter
- [x] Manual DIP switch programming of RAM chip
- [x] Output from RAM chip
- [x] Automatic programming of RAM chip using Raspberry Pi zero [^2]
- [x] Manual data input via DIP switch
- [x] 1 bit push button for data bus
- [x] result bit
- [x] testing
- [ ] Scratch register
- [ ] Scratch register display
- [ ] Output register
- [ ] Output register display
- [ ] more testing

### Issues to fix
<br>

- [ ] Add diodes to programming bus
- [ ] Detach Raspberry Pi pico 5V from USB and take from main power rails (keep GND via USB)

### Cosmetic / documentation
<br>

- [X] Order acrylic base
- [X] Mount acrylic base
- [ ] Labels
- [ ] Graphics

[^1]: https://www.youtube.com/playlist?list=PLnw98JPyObn1GUapiXLlGm8RrpQF-J_c1

<br>

[^2]: This also included the steps needed to prevent two signals writing to the programming bus at the same time
