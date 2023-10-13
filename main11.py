class player:
  def play(|Self):
    printf("the player is playing cricket")
    class batsman(player):
      def play(self):
        printf("the batsman is batting")
        class bowler(|player):
          def play(Self):
            print("the bowler is bowling")
            batsman=batsman()
            bowler=bowler()
            batsman.play()
            bowler.play()