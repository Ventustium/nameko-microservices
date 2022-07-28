-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Jul 28, 2022 at 09:55 AM
-- Server version: 5.7.38
-- PHP Version: 8.0.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nameko_library`
--
CREATE DATABASE IF NOT EXISTS `nameko_library` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `nameko_library`;

-- --------------------------------------------------------

--
-- Table structure for table `lightnovelLibrary`
--

CREATE TABLE `lightnovelLibrary` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext,
  `status` varchar(10) DEFAULT NULL,
  `verif` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lightnovelLibrary`
--

INSERT INTO `lightnovelLibrary` (`id`, `title`, `description`, `status`, `verif`) VALUES
(1, 'Gakusen Toshi Asterisk', 'In the previous century, an unprecedented disaster known as the Invertia drastically reformed the world. The powers of existing nations declined significantly, paving the way for a conglomerate called the Integrated Empire Foundation to assume control. But more importantly, the Invertia led to the emergence of a new species of humans who are born with phenomenal physical capabilities—the Genestella. Its elite are hand-picked across the globe to attend the top six schools, and they duel amongst themselves in entertainment battles called Festas.\n\nAyato Amagiri is a scholarship transfer student at the prestigious Seidoukan Academy, which has recently been suffering from declining performances. Through a series of events, he accidentally sees the popular Witch of Resplendent Flames, Julis-Alexia von Riessfeld, half-dressed! Enraged, Julis challenges him to a duel for intruding on her privacy. After said duel is voided by the student council president, Ayato reveals that he has no interest in Festas. Instead, he has enrolled in the academy to investigate the whereabouts of his missing elder sister. But when a more devious plot unravels, Ayato sets out to achieve victory, while being surrounded by some of the most talented Genestella on the planet.', NULL, 1),
(2, 'Date a Live', 'This is date a Live 2', NULL, 1),
(4, 'Strike the Blood', 'No Description', NULL, 1),
(6, '86 -eightysix-', 'According to the Republic of San Magnolia, their ongoing war against the Giadian Empire has no casualties—however, that is mere propaganda. While the silver-haired Alba of the Republic\'s eighty-five sectors live safely behind protective walls, those of different appearances are interned in a secret eighty-sixth faction. Known within the military as the Eighty-Six, they are forced to fight against the Empire\'s autonomous Legion under the command of the Republican \"Handlers.\"\n\nVladilena Milizé is assigned to the Spearhead squadron to replace their previous Handler. Shunned by her peers for being a fellow Eighty-Six supporter, she continues to fight against their inhumane discrimination. Shinei Nouzen is the captain of the Spearhead squadron. Infamous for being the sole survivor of every squadron he\'s been in, he insists on shouldering the names and wishes of his fallen comrades. When the fates of these young souls from two different worlds collide, will it ignite the spark that lights their path to salvation, or will they burn themselves in the flames of despair?\n\n[Written by MAL Rewrite]', NULL, 1),
(7, 'Accel World ', 'Haruyuki Arita is an overweight, bullied middle schooler who finds solace in playing online games. But his life takes a drastic turn one day, when he finds that all his high scores have been topped by Kuroyukihime, the popular vice president of the student council.', NULL, 1),
(8, 'Absolute Duo', 'Individuals who can materialize weapons from their soul are called \"Blazers,\" and they attend Kouryou Academy High School in order to harness their abilities. Each student is required to partner with another, in the hopes that one day, the pair can attain the power of Absolute Duo.\n\nTooru Kokonoe hopes to attend this academy in order to gain power after his sister and friends were slain by a mysterious man. However, at the opening ceremony, he is forced to duel against the person sitting next to him, with the loser being expelled. As Tooru prepares to give the match his all, it is not a weapon that manifests from his soul, but a shield, an irregularity which catches the attention of a foreign student named Julie Sigtuna.\n\n[Written by MAL Rewrite]', NULL, 1),
(9, 'Ao no Exorcist', 'No Description', NULL, 1),
(10, 'Arifureta Shokugyou de Sekai Saikyou', 'The ordinary life of 17-year-old otaku Hajime Nagumo is disrupted when he and his classmates are summoned to a fantasy world and tasked with saving mankind. While his classmates are gifted with impressive abilities useful in combat, Hajime is belittled for only gaining an inferior transmutation skill that lacks any real offensive power.\n\nDuring an expedition in the Great Orcus Labyrinth, Hajime is betrayed by one of his classmates, plummeting him to the bottom of an abyss. Though he survives the fall, Hajime is faced with menacing monsters and misfortunes that send him spiraling into a grim nightmare. Desperate to live and return home one day, he resolves to fight for his survival—only to meet an imprisoned vampire he names Yue, who is also seeking to escape the labyrinth. Taking an interest in him, Yue and a few others along the way accompany Hajime on his journey to find a way back home, while steadily transforming from commonplace to the world\'s strongest.\n\n[Written by MAL Rewrite]', NULL, 1),
(11, 'Arifureta Shokugyou de Sekai Saikyou Zero', 'No Description', NULL, 1),
(12, 'Asahina Wakaba to Marumaru na Kareshi', 'No Description', NULL, 1),
(15, 'Ascendance of a Bookworm', 'This is the Description', NULL, 1),
(16, 'Baka to Test to Shoukanjuu ', 'No Description', NULL, 1),
(17, 'Banished from the Hero’s Party, I Decided to Live a Quiet Life in the Countryside', 'No Description', NULL, 1),
(18, 'Beatless', 'No Description', NULL, 1),
(19, 'Hataraku Maou-sama!', 'Do you want fries with your hellfire? Being soundly thrashed by the hero Emilia, the Devil King and his general beat a hasty retreat to a parallel universe...only to land smack in the middle of bustling, modern-day Tokyo! Lacking the magic necessary to return home, the two are forced to assume human identities and live average human lives until they can find a better solution. And to make ends meet, Satan finds gainful employment at a nearby fast food joint! With his devilish mind set on working his way up the management food chain, what will become of his thirst for conquest?!', NULL, 1),
(20, 'Black Bullet', 'In the year 2021, mankind is ravaged by the epidemic of Gastrea, a parasitic virus, and is forced to live within the Monolith walls, which are created from Varanium: a metal that is able to subdue Gastrea. Soon, children who were born with the Gastrea virus and obtained superhuman abilities as a result, are discovered and dubbed \"Cursed Children\". Due to the Gastrea virus\' intervention, the Cursed Children could only be female. Civil Securities are formed to specialize fighting against Gastrea, operating with the pair of an Initiator, who are cursed children, and a Promoter, serving to lead the cursed children. Ten years after the epidemic, Rentarō Satomi, a high school student who is also a Promoter in Tendō Civil Security Agency owned by his childhood friend Kisara Tendō, along with his Initiator, Enju Aihara, conducts missions to prevent the destruction of the Tokyo Area and the world.', NULL, 1),
(21, 'Bofuri: I Don’t Want to Get Hurt, so I’ll Max Out My Defense', 'No Description', NULL, 1),
(22, 'Boku no Hero Academia Yuuei Hakusho', 'No Description', NULL, 1),
(23, 'Campione', 'No Description', NULL, 1),
(24, 'Drugstore in Another World', 'No Description', NULL, 1),
(25, 'Ero Manga Sensei', 'No Description', NULL, 1),
(26, 'Goblin Slayer', 'No Description', NULL, 1),
(27, 'Hentai Ouji to Warawanai Neko', 'No Description', NULL, 1),
(28, 'Hidan no Aria', 'No Description', NULL, 1),
(29, 'Hundred', 'No Description', NULL, 1),
(30, 'Hyouka', 'No Description', NULL, 1),
(31, 'Infinite Stratos', 'No Description', NULL, 1),
(32, 'Isekai Maou to Shoukan Shoujo no Dorei Majutsu', 'No Description', NULL, 1),
(33, 'Isekai wa Smartphone to Tomo ni.', 'No Description', NULL, 0),
(34, 'Kimi no Na wa.', 'No Description', NULL, 1),
(35, 'Kokoro Connect', 'No Description', NULL, 1),
(36, 'knights and Magic', 'No Description', NULL, 1),
(37, 'Kumo Desu ga, Nani ka?', 'No Description', NULL, 1),
(38, 'Kuma Kuma Kuma Bear', 'No Description', NULL, 1),
(39, 'Log Horizon', 'No Description', NULL, 1),
(40, 'Magic Gems Gourmet', 'No Description', NULL, 1),
(41, 'My Status as an Assassin Obviously Exceeds the Hero’s', 'No Description', NULL, 1),
(42, 'My Stepmom’s Daughter Is My Ex', 'No Description', NULL, 1),
(43, 'My Stepsister is My Ex-Girlfriend', 'No Description', NULL, 1),
(44, 'Nanatsu no Taizai', 'No Description', NULL, 1),
(45, 'No Game No Life', 'No Description', NULL, 1),
(46, 'Only Sense Online', 'No Description', NULL, 1),
(48, 'I’m Gonna Live with You Not Because My Parents Left Me Their Debt But Because I Like You', 'The main character, Yoshizumi Yuya, was being pressured into paying off the debt left by his parents who had fled abroad. It was his classmate, Hitotsuba Kaede, chosen as the cutest schoolgirl in Japan, who saved him from this crisis of life and death. However, there was a catch. The condition required to fulfill in return for taking over his debt was — “In return for the loan, you have – to live with me.”\r\n\r\n“Why did that happen?!”\r\n\r\nYuya’s daily life collapsed on this day.\r\n\r\n“Yuya-kun. Let’s take a bath together.”\r\n\r\n“Yuya-kun, please be my hug pillow.”\r\n\r\n“That’s enough, Hitotsuba-san!”\r\n\r\nThe slapstick love comedy between the beautiful, but easy-going Hitotsuba Kaede and the serious and hard-headed Yoshizumi Yuya, starts now!', NULL, 1),
(49, 'Saijaku Muhai no Bahamut', 'Lux, a former prince of an empire named Arcadia that was overthrown via a rebellion five years earlier, accidentally trespasses in a female dormitory\'s bathing area, sees the kingdom\'s new princess Lisesharte naked, incurring her wrath. Lisesharte then challenges Lux to a Drag-Ride duel. Drag-Rides are ancient armored mechanical weapons that have been excavated from ruins all around the world. Lux used to be called the strongest Drag-Knight, but now he\'s known as the \"undefeated weakest\" Drag-Knight because he will absolutely not attack in battle. After his duel with Lisesharte, Lux ends up attending the female-only academy that trains royals to be Drag-Knights. (Source: ANN)', NULL, 1),
(50, 'Potion-danomi de Ikinobimasu!', 'Kaoru Nagase was caught up in a mysterious phenomenon and died when returning home from work. It was because of a time-space distortion that a higher life form was cleaning up, but she was able to receive a younger body and the ability to create any potion she wanted in another world!\n\n(Source: MangaDex)', NULL, 1),
(65, 'Omiai Shitakunakattanode, Muri Nandai na Jouken wo Tsuketara Doukyuusei ga Kita Ken ni Tsuite', 'One day, Yuzuru Takasegawa — a first-year high school student — is urged by his grandfather to go on an arranged marriage meeting, insisting that he wants to see his great-grandson before he dies. \n However, not wanting to bear the weight of a fiancee at the tender age of a freshman in high school, Yuzuru tries to avoid the arranged marriage meeting by imposing an irrational condition that, “If she is Blonde Haired, Blue Eyed, Fair Skinned etc., only then I will think about the marriage ”.But somehow, he finds the girl who meets the conditions that Yuzuru has put out, and he reluctantly ends up going to matchmaking only once. And on the day of matchmaking, it was Arisa Yukishiro, a beautiful girl with reputation at school, shows up on the scene. Upon hearing her story, it seems she was also reluctantly made to go on matchmaking. Therefore, the two of them try to prevent themselves from further marriage proposals with their false “engagement”. And so, as they play the role of fake lovers, they find themselves in love with each other and become real lovers. \n\nSource: Syosetu', NULL, 1),
(72, 'Death\'s Daughter and the Ebony Blade', 'Olivia is just a baby when the mysterious Z finds her at a temple in the depths of the Forest of No Return. From that day on, the temple becomes her home and Z her family. Z, a god of death, educates her in the ways of the world, in combat, and in the long-forgotten arts of magic—right up until the day Z disappears. Olivia leaves the forest for the first time in search of Z with its ebony blade in hand. Out in the wider world, all is not well. A bitter war rages between the Asvelt Empire and the Kingdom of Fernest, and Fernest is losing badly. When Olivia shows up on Fernest’s doorstep with a sack of imperial heads looking to volunteer, the royal army happily welcomes her into its ranks. Thanks to Z’s training, she quickly proves herself as a ferocious warrior. In fact, she might be just what Fernest needs to turn the tide of the war...but will they accept her lack of people skills and disregard for discipline? And will she ever see Z again?', NULL, 1),
(73, 'Full Metal Panic', 'Sagara Sousuke isn\'t your typical high school student. He reads military enthusiast magazines; he responds to questions with \"affirmative;\" he brings grenades to school in his bag. Though everyone at school takes him for a hopeless military geek, Chidori Kaname thinks there might be something more to him. When their plane is hijacked in the middle of a field trip, Kaname\'s instincts will prove correct: Sousuke is an elite, mech-piloting mercenary... and he\'s here to protect her!', NULL, 1),
(74, 'Seventh', 'In a world of swords and magic, where the Goddess is revered, Lyell Walt was fortunate enough to be born the first son and heir to an earldom. That is, until his parents disown him for losing pitifully in a fight with his younger sister, Ceres. Lyell had once been hailed as a prodigy—a wonder child—but the birth of his sister changed everything. After Ceres wounds him in their duel, an enigmatic old man swoops in to rescue Lyell and bestows upon him a necklace containing a jewel that has been blessed by the goddesses and passed down through the last seven generations of Walt leaders. As Lyell sets out, necklace in hand, will he be able to prove himself despite his humiliating loss to his sister? And moreover, will he be able to solve the mystery behind Ceres’s monstrous strength and the strange sway she seems to hold over his entire family?', NULL, 1),
(75, 'Backstabbed in a Backwater Dungeon', 'When Light is kicked out of the Concord of the Tribes, his former comrades instantly turn on him. Light escapes this diabolical act of betrayal by the skin of his teeth...only to find himself in the deepest part of the Abyss, the most dangerous dungeon in the realm! To avoid being eaten by carnivorous monsters, he uses the Unlimited Gacha, his sole magical skill. But where it previously only produced junk items, this time Mei—a gorgeous Level 9999 fighter in a maid outfit—springs forth! Fast forward three years and Light has carved out his own kingdom in this backwater dungeon, summoning more beautiful Level 9999 warriors who swear absolute fealty to him. Now a powerful Level 9999 Overlord himself, Light plans to ascend to the surface and take revenge on his betrayers one by one!', NULL, 1),
(76, 'I’m a NEET but When I Went to Hello Work I Got Taken to Another World (LN)', 'The NEET Yamano Masaru (23 years old) went to Hello Work and found an interesting job offer. [A sword and sorcery fantasy, test play for Miniature Garden of Razgrad. Extended period of time, preferred to be able to live on site. Monthly salary of 250,000+]. He immediately went to the interview and signed a contract.\n\nHowever, the place of employment is in another world. Because of the contract, he’s taken there, and in order to survive, Masaru received a cheat but is told the shocking truth.\n\n“This world will be destroyed in 20 years.”\n\nCan a simple NEET prevent the destruction of the world!?', NULL, 1),
(77, 'In Another World with My Smartphone', 'Mochizuki Touya, a 15-year-old boy, who got zapped by a flash of lightning due to a freak accident caused by God, wakes up and finds himself face-to-face with God.\n\n“I am afraid to say that I have made a blunder…” laments the old coot. In order to smooth over the fault, God says that he can reincarnate Touya into a world of fantasy, and allow Touya to bring the smartphone! Then in a new, anachronistic pseudo-medieval world begins Touya’s adventure.\n\nFriends! Laughs! Tears! Inexplicable Deus ex Machina! Mochizuki Touya sets off on a journey full of wonder as he absentmindedly travels from place to place, following whatever goal catches his fancy. The curtains on an epic tale of swords, sorcery, and smartphone apps lift!', NULL, 1),
(78, 'The Gal Is Sitting Behind Me, and Loves Me (LN)', 'No common contact whatsoever, and I got liked by her… and my school life got drastically changed!?\n\nHaving been spending my days only studying without even a single friend, I saved her out of just a mere whim.\n\nThat’s how it should be, but—\n\n“I could hardly wait for after school! …Hey, kiss me.”\n\nThat incident led me to start dating Shino.\n\nSpending time together after school, going along with each other’s hobbies, frequent sleepovers…\n\nShe is kind and always sticks to me.\n\nMoreover, my classmates took notice of me, gave me a makeover, and my surroundings also got noisy.\n\nIt’s making me more restless than when I was alone, but… well, I guess this kinda school life is also not bad.', NULL, 1),
(79, 'The Gal Is Sitting Behind Me, and Loves Me (WN)', 'No common contact whatsoever, and I got liked by her… and my school life got drastically changed!?\n\nHaving been spending my days only studying without even a single friend, I saved her out of just a mere whim.\n\nThat’s how it should be, but—\n\n“I could hardly wait for after school! …Hey, kiss me.”\n\nThat incident led me to start dating Shino.\n\nSpending time together after school, going along with each other’s hobbies, frequent sleepovers…\n\nShe is kind and always sticks to me.\n\nMoreover, my classmates took notice of me, gave me a makeover, and my surroundings also got noisy.\n\nIt’s making me more restless than when I was alone, but… well, I guess this kinda school life is also not bad.', NULL, 1),
(80, 'The Girl Who Was Supposed to Confess Her Love to Me as a Punishment Game, But No Matter How You Look at It, She’s in Love With Me!', 'Misumai Youshin, a boy with a negative personality, starts going out with Barato Nanami, a prim and proper type gyaru who is at the top of the class caste.\n\nBut as a matter of fact, the confession was part of a punishment game!?\n\nAnd yet, Nanami, who he thought was a gyaru, was only a gyaru in appearance; in truth, she was not good with men!\n\nBut the way they met in the morning, went to school together and ate their lunches together, none of this appeared to be a punishment; Nanami looked deeply in love with Youshin――!?\n\nThis is a super sweet love story that starts with two beginners in love!\n\n陰キャの僕に罰ゲームで告白してきたはずのギャルが、どう見ても僕にベタ惚れです\nAuthor: 結石 (Yuishi) | Illustrator: かがちさく (Kaga Chisaku)', NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lightnovelLibrary`
--
ALTER TABLE `lightnovelLibrary`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lightnovelLibrary`
--
ALTER TABLE `lightnovelLibrary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
