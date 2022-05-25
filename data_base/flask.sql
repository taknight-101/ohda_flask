-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 17, 2021 at 03:03 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `assistant`
--

DROP TABLE IF EXISTS `assistant`;
CREATE TABLE IF NOT EXISTS `assistant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`teacher_id`)
) ENGINE=MyISAM AUTO_INCREMENT=355 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assistant`
--

INSERT INTO `assistant` (`id`, `full_name`, `email`, `phone`, `stage`, `img`, `teacher_id`) VALUES
(278, 'Jeffrey Wiggins MD', 'robertstokes@watson-phillips.com', '71498278182', 1, NULL, 1),
(277, 'Kyle Hurley', 'tyrone29@hotmail.com', '99208391892', 1, NULL, 1),
(276, 'Andrea Krause', 'zphillips@mcdonald.net', '59995576393', 1, NULL, 1),
(275, 'Joshua Wilson', 'hmurray@martinez-hinton.com', '34850387800', 1, NULL, 1),
(274, 'Peggy Murphy', 'stephaniepark@wallace-green.com', '73339678123', 1, NULL, 1),
(273, 'Thomas Stewart', 'xknight@hotmail.com', '62904913443', 1, NULL, 1),
(272, 'Robert Guerra', 'stephenhopkins@hanson.biz', '96328996016', 1, NULL, 1),
(271, 'Kenneth Moore', 'wcervantes@yahoo.com', '40377781496', 1, NULL, 1),
(270, 'Danielle Johnson', 'ucruz@rose.com', '14956828035', 1, NULL, 1),
(269, 'Carly Mcknight', 'kfranco@bonilla-wilson.com', '43270594267', 1, NULL, 1),
(268, 'Julie Anderson', 'jeff20@kennedy.com', '17221511555', 1, NULL, 1),
(267, 'Regina Cummings', 'burkestefanie@hill.com', '73539921575', 1, NULL, 1),
(266, 'Patricia Davis', 'fordkristin@clark-smith.com', '93099044599', 1, NULL, 1),
(265, 'Elizabeth Calhoun', 'nelsonstephanie@spencer-vasquez.org', '35647307498', 1, NULL, 1),
(264, 'John Garner', 'amandamiller@roberts-tran.com', '66079707385', 1, NULL, 1),
(263, 'Robert Baldwin', 'rowebrandy@yahoo.com', '97433938781', 1, NULL, 1),
(262, 'Joel Moore', 'estradajeffrey@cole.com', '70581700295', 1, NULL, 1),
(261, 'Michelle Morris', 'iphillips@clay-nguyen.com', '36379018878', 1, NULL, 1),
(260, 'Tyler Smith', 'hsantos@moody.com', '36881541607', 1, NULL, 1),
(259, 'Mitchell Hogan', 'jeffrey90@taylor.info', '99998635220', 1, NULL, 1),
(258, 'Billy Wade', 'jacob05@young.info', '76529526982', 1, NULL, 1),
(257, 'Jim Thompson', 'tracyhayden@little.com', '07952695223', 1, NULL, 1),
(256, 'Adrienne Washington', 'sonyaklein@gmail.com', '76883132330', 1, NULL, 1),
(255, 'Jordan Holt', 'amandascott@nguyen.com', '72597874006', 1, NULL, 1),
(254, 'Patricia Wood', 'iray@garcia.com', '65226613461', 1, NULL, 1),
(253, 'Jonathan Maxwell', 'billy20@yahoo.com', '02572098911', 1, NULL, 1),
(252, 'Jeffrey Jones', 'brandon21@gomez.com', '51877252816', 1, NULL, 1),
(251, 'Amanda Hines', 'olivertina@wang.org', '61148838108', 1, NULL, 1),
(250, 'Charles Evans', 'josecampbell@glass.com', '68190615940', 1, NULL, 1),
(249, 'Christina Alvarez MD', 'donald76@hotmail.com', '39788444564', 1, NULL, 1),
(242, 'Denise Mathis', 'mdavidson@gmail.com', '61130852390', 1, NULL, 1),
(243, 'Kristen Jordan', 'anthonysanders@gmail.com', '70926982064', 1, NULL, 1),
(244, 'Ryan Fritz', 'nicolekelly@yahoo.com', '52692229149', 1, NULL, 1),
(245, 'Barbara Cherry', 'greenamy@gmail.com', '17157297044', 1, NULL, 1),
(246, 'Lori Garcia', 'thomastheresa@hotmail.com', '30596658325', 1, NULL, 1),
(247, 'Walter Soto', 'anita83@gmail.com', '31450922427', 1, NULL, 1),
(248, 'Yolanda Mayo', 'gregoryangela@bailey.com', '90280548183', 1, NULL, 1),
(235, 'Arthur Perez', 'john54@soto-smith.com', '81857957803', 1, NULL, 1),
(236, 'David Thomas', 'pereztyler@thomas.com', '13927846611', 1, NULL, 1),
(237, 'Frank Long', 'waltersandra@yahoo.com', '01915701611', 1, NULL, 1),
(238, 'Zachary Price', 'kellyhaley@yahoo.com', '83015168954', 1, NULL, 1),
(239, 'Mrs. Martha Porter', 'jillkirk@hughes.com', '43205619066', 1, NULL, 1),
(240, 'Christina Mccormick', 'michael78@gmail.com', '28978850747', 1, NULL, 1),
(241, 'Dean Phillips', 'bgarcia@austin.com', '13269644765', 1, NULL, 1),
(234, 'Dillon Hughes', 'christinachan@roberts.org', '39176374982', 1, NULL, 1),
(233, 'Gabriel Davis', 'vtaylor@alvarado.com', '54614398422', 1, NULL, 1),
(232, 'Patricia Mayer', 'ronniemartinez@lee-harvey.com', '72071222721', 1, NULL, 1),
(231, 'Louis Mclaughlin', 'kevin14@arias.com', '36352703552', 1, NULL, 1),
(230, 'Samantha Cox', 'patrickbarnes@yahoo.com', '11897342469', 1, NULL, 1),
(228, 'Lisa Fischer', 'jesse22@evans-mcclain.org', '97285222338', 1, NULL, 1),
(229, 'Christopher Porter', 'jamesmoore@hotmail.com', '62495335535', 1, NULL, 1),
(227, 'John Perez', 'john41@beard-tucker.com', '04375996603', 1, NULL, 1),
(226, 'Pamela Jones', 'erica23@yahoo.com', '76901783378', 1, NULL, 1),
(225, 'Elizabeth Graves', 'ucruz@bryan-tran.com', '99855665188', 1, NULL, 1),
(224, 'Tony Anderson', 'xbarker@potts.info', '69825795310', 1, NULL, 1),
(223, 'Troy Wheeler', 'cassandra32@jackson-phillips.biz', '92262499223', 1, NULL, 1),
(222, 'Michelle Humphrey', 'kristina74@johnson-powell.com', '16857294297', 1, NULL, 1),
(221, 'Christopher Duran', 'victoria74@yahoo.com', '94932976528', 1, NULL, 1),
(220, 'Arthur Campos', 'mikesawyer@murphy-smith.com', '72433410997', 1, NULL, 1),
(219, 'Selena Roach', 'hmitchell@yahoo.com', '78253933049', 1, NULL, 1),
(218, 'Joe Roberts', 'james68@alvarez.com', '49586362616', 1, NULL, 1),
(217, 'Ashley Christensen', 'curtis36@hotmail.com', '19365506670', 1, NULL, 1),
(216, 'Sarah Gomez', 'salazarjeffrey@gmail.com', '22640752448', 1, NULL, 1),
(215, 'Ana Wade', 'johnsonpeter@price-harris.com', '80054231573', 1, NULL, 1),
(214, 'Tyler Rivera', 'allendeborah@gmail.com', '27269766623', 1, NULL, 1),
(213, 'Tammy Ramos', 'kflores@pierce-villa.com', '70802239852', 1, NULL, 1),
(212, 'Sarah Jones', 'russelljamie@gmail.com', '23664776596', 1, NULL, 1),
(211, 'Sheryl Christian', 'xbaker@ferrell.net', '41578907825', 1, NULL, 1),
(210, 'Ian Simpson', 'nancygonzales@phelps-gardner.biz', '50084445924', 1, NULL, 1),
(209, 'Kayla Duncan', 'anthony48@hotmail.com', '55512360184', 1, NULL, 1),
(208, 'Arthur Dawson', 'cunninghamstephanie@lawson-buchanan.com', '23367381820', 1, NULL, 1),
(207, 'Theresa Gomez', 'anthony81@anderson.com', '35222126535', 1, NULL, 1),
(206, 'Melissa Ramirez', 'lorivaldez@contreras.com', '49115382055', 1, NULL, 1),
(205, 'Mr. Bruce Jones', 'bryanburke@hotmail.com', '11097728354', 1, NULL, 1),
(279, 'John Le', 'joshuaweber@sanchez-morgan.info', '68839620800', 1, NULL, 1),
(280, 'Theresa Guerrero', 'jacksonlisa@snyder.com', '66322757234', 1, NULL, 1),
(281, 'Joseph Wyatt', 'karen07@dixon-castro.info', '21533415869', 1, NULL, 1),
(282, 'Lynn Griffin', 'hollandtaylor@hotmail.com', '04842525159', 1, NULL, 1),
(283, 'April Williams', 'lindasanders@yahoo.com', '30578892469', 1, NULL, 1),
(284, 'Adam Vasquez', 'gcummings@madden-kelly.com', '69048745460', 1, NULL, 1),
(285, 'Rodney Hansen', 'nathanlong@davies-dixon.com', '62467552684', 1, NULL, 1),
(286, 'Ethan Adams', 'francis35@lopez-stafford.net', '87669498186', 1, NULL, 1),
(287, 'Derrick Smith', 'yuteresa@jenkins-rojas.net', '23723335282', 1, NULL, 1),
(288, 'Paul Harris', 'amyhernandez@ramirez.biz', '46315256148', 1, NULL, 1),
(289, 'Michelle Gonzalez', 'jessicawatson@yahoo.com', '04991685631', 1, NULL, 1),
(290, 'Andrew Torres', 'cmcclure@yahoo.com', '43303520239', 1, NULL, 1),
(291, 'Holly Miller', 'uhicks@gmail.com', '77764470547', 1, NULL, 1),
(292, 'Oscar Powers', 'tammybrady@miller-avila.com', '72282639048', 1, NULL, 1),
(293, 'Ryan Berry', 'deanwilson@reynolds.com', '21725373659', 1, NULL, 1),
(294, 'Robert Robinson', 'brownbrent@smith-wilson.biz', '91246601383', 1, NULL, 1),
(295, 'Kelly Clark', 'kylejones@yahoo.com', '92491148661', 1, NULL, 1),
(296, 'Patrick Combs', 'hatfieldgina@gmail.com', '67842447684', 1, NULL, 1),
(297, 'Nathan Poole', 'vjones@jones-vasquez.info', '79318657165', 1, NULL, 1),
(298, 'John Juarez', 'hansenchristopher@alvarado.com', '96892685373', 1, NULL, 1),
(299, 'Karen Hale', 'christophercooper@gmail.com', '47064369807', 1, NULL, 1),
(300, 'Mark Horn', 'rachel45@smith-jones.com', '11494447101', 1, NULL, 1),
(301, 'Denise Cox', 'gomezjoshua@hotmail.com', '11835161155', 1, NULL, 1),
(302, 'Mrs. Nicole Dixon DDS', 'huntfaith@rice.biz', '84207242811', 1, NULL, 1),
(303, 'Mrs. Shannon Franklin', 'thomasamanda@gmail.com', '08625124227', 1, NULL, 1),
(304, 'Clayton Davis', 'michele05@white.info', '83913812216', 1, NULL, 1),
(305, 'Caitlin Benson', 'downscole@yahoo.com', '23449970520', 1, NULL, 1),
(306, 'Roy Ross', 'pamelamorris@cain.biz', '89350557216', 1, NULL, 1),
(307, 'Kimberly Hicks', 'shellyrobinson@thomas-fuller.com', '32368870039', 1, NULL, 1),
(308, 'Beverly Willis', 'marioramos@hotmail.com', '39840965345', 1, NULL, 1),
(309, 'Elizabeth Yu', 'tyler01@hotmail.com', '19212817378', 1, NULL, 1),
(310, 'Nancy Trujillo', 'vargasryan@molina-clements.com', '24020377284', 1, NULL, 1),
(311, 'Megan Johnson', 'mfox@gmail.com', '30687130597', 1, NULL, 1),
(312, 'Dr. Joseph Ruiz', 'hawkinsshannon@yahoo.com', '42729127353', 1, NULL, 1),
(313, 'Matthew Gray', 'jonathon62@young-ferguson.info', '85519902961', 1, NULL, 1),
(314, 'Karen Lopez', 'andrew53@davis.org', '32364423903', 1, NULL, 1),
(315, 'Joshua Green', 'wrightjennifer@yahoo.com', '86119663383', 1, NULL, 1),
(316, 'Sharon Smith', 'karlgrant@hotmail.com', '28334376898', 1, NULL, 1),
(317, 'Brittany Hansen', 'carlmarquez@gmail.com', '47045677966', 1, NULL, 1),
(318, 'Stacey Beard', 'whitejeffrey@hotmail.com', '80600976045', 1, NULL, 1),
(319, 'Nicholas Graham', 'oayers@bailey-wells.com', '81912777649', 1, NULL, 1),
(320, 'Thomas Edwards', 'matthew98@hotmail.com', '20770756355', 1, NULL, 1),
(321, 'Brett Diaz', 'hmclaughlin@hotmail.com', '69415193836', 1, NULL, 1),
(322, 'Jeffrey Bowers', 'jamestaylor@williams-henry.com', '16094947443', 1, NULL, 1),
(323, 'Anthony Bridges', 'brandonwelch@wilcox.info', '44401475081', 1, NULL, 1),
(324, 'Monica Elliott', 'ocombs@walker-mason.info', '19758196325', 1, NULL, 1),
(325, 'Randall Hess', 'whowell@miller.info', '49912577848', 1, NULL, 1),
(326, 'Jonathan Hall', 'torreschris@davis.com', '88533666818', 1, NULL, 1),
(327, 'Kevin Pierce', 'daniel12@walker.org', '05120204849', 1, NULL, 1),
(328, 'James Williams', 'bwilkins@yahoo.com', '19372986374', 1, NULL, 1),
(329, 'Anna Price', 'ugreen@gonzalez.biz', '65967549164', 1, NULL, 1),
(330, 'Mark Nunez', 'johnmurray@bryant-brown.biz', '02800631432', 1, NULL, 1),
(331, 'Claudia Wilson', 'mcintoshrichard@gmail.com', '95693460732', 1, NULL, 1),
(332, 'Todd Meadows', 'lindaharmon@hotmail.com', '48380997071', 1, NULL, 1),
(333, 'Ryan Mitchell', 'alexis01@hotmail.com', '96883346252', 1, NULL, 1),
(334, 'Kenneth Thomas', 'robertstewart@gmail.com', '40995644923', 1, NULL, 1),
(335, 'Anthony Davis Jr.', 'lori69@gmail.com', '83396131553', 1, NULL, 1),
(336, 'Christopher Stewart', 'teresahowell@johnson.com', '86227700114', 1, NULL, 1),
(337, 'Hannah Fernandez', 'michael20@brown-juarez.com', '55691394528', 1, NULL, 1),
(338, 'Jennifer Ingram MD', 'brookebrock@gmail.com', '57080319351', 1, NULL, 1),
(339, 'Kevin Lewis', 'ashleyhall@gmail.com', '67621924093', 1, NULL, 1),
(340, 'Susan Green', 'summersjulie@yahoo.com', '78109866969', 1, NULL, 1),
(341, 'Ryan Daniel', 'jefferygonzalez@trujillo.org', '74823792370', 1, NULL, 1),
(342, 'Andres Mckinney', 'garyperkins@gmail.com', '80145535503', 1, NULL, 1),
(343, 'Christopher Jones', 'adrianwhite@gmail.com', '54257663987', 1, NULL, 1),
(344, 'Caleb Smith', 'esmith@gmail.com', '13379320118', 1, NULL, 1),
(345, 'Christine Smith', 'mooreshannon@hotmail.com', '88575879951', 1, NULL, 1),
(346, 'Howard Randolph', 'ibarton@gmail.com', '06212189701', 1, NULL, 1),
(347, 'Brittney Gilmore', 'roy76@gmail.com', '07876602064', 1, NULL, 1),
(348, 'Jennifer Smith', 'whayes@gmail.com', '64107547052', 1, NULL, 1),
(349, 'Regina Mcconnell', 'ibarrachad@williams.com', '43833508745', 1, NULL, 1),
(350, 'Trevor Davis', 'lcoleman@hotmail.com', '60215642906', 1, NULL, 1),
(351, 'Cynthia Miller', 'peteradams@hill-stevenson.info', '52102039269', 1, NULL, 1),
(352, 'Michael Arroyo', 'jermaine08@robinson-moore.net', '51825175138', 1, NULL, 1),
(353, 'Robert Smith', 'chadholland@yahoo.com', '60292040313', 1, NULL, 1),
(354, 'Richard Harper', 'albertanderson@delacruz.org', '22419414530', 1, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `center`
--

DROP TABLE IF EXISTS `center`;
CREATE TABLE IF NOT EXISTS `center` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `center_subscription`
--

DROP TABLE IF EXISTS `center_subscription`;
CREATE TABLE IF NOT EXISTS `center_subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `center_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  KEY `center_id` (`center_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
CREATE TABLE IF NOT EXISTS `coupon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `exprie_after` timestamp NULL DEFAULT NULL,
  `exprie_at` timestamp NULL DEFAULT NULL,
  `used` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
CREATE TABLE IF NOT EXISTS `exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `homework`
--

DROP TABLE IF EXISTS `homework`;
CREATE TABLE IF NOT EXISTS `homework` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `live_meeting`
--

DROP TABLE IF EXISTS `live_meeting`;
CREATE TABLE IF NOT EXISTS `live_meeting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `lock_materilas`
--

DROP TABLE IF EXISTS `lock_materilas`;
CREATE TABLE IF NOT EXISTS `lock_materilas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `locking_preiod` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `parent`
--

DROP TABLE IF EXISTS `parent`;
CREATE TABLE IF NOT EXISTS `parent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `student_id` int(11) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=151 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parent`
--

INSERT INTO `parent` (`id`, `full_name`, `student_id`, `phone`, `stage`) VALUES
(1, 'Denise Sweeney', 0, '76506033920', 1),
(2, 'Amy Morris', 1, '42356627125', 1),
(3, 'Mark Bryan', 2, '05377654876', 1),
(4, 'Heather Kim', 3, '53990290893', 1),
(5, 'Shannon Boyd', 4, '91049721139', 1),
(6, 'William Pennington', 5, '75206522934', 1),
(7, 'Ashley Huang', 6, '88007053825', 1),
(8, 'Robin Lopez', 7, '06357103263', 1),
(9, 'Sarah Allen', 8, '09272010031', 1),
(10, 'Oscar Patel', 9, '16497405787', 1),
(11, 'Allison Shelton', 10, '88407076794', 1),
(12, 'Joshua Barnes', 11, '55344011624', 1),
(13, 'Daniel Figueroa', 12, '14503284324', 1),
(14, 'Erin Gardner', 13, '40062848987', 1),
(15, 'Mr. Christopher Graham Jr.', 14, '69177078391', 1),
(16, 'Joshua Barrett', 15, '65663673537', 1),
(17, 'Nicole Gates', 16, '89473396011', 1),
(18, 'Danielle Burgess', 17, '52807924215', 1),
(19, 'Carla Rogers', 18, '22883658518', 1),
(20, 'Hannah Caldwell', 19, '85440189984', 1),
(21, 'Steven Taylor', 20, '26721523529', 1),
(22, 'Bradley Jones', 21, '03804028813', 1),
(23, 'Randy Pruitt', 22, '37030619790', 1),
(24, 'John Rogers', 23, '40286302818', 1),
(25, 'Stephen Wade', 24, '52390019057', 1),
(26, 'Stacy Frost', 25, '24713768303', 1),
(27, 'Stephanie Bowman', 26, '90220033717', 1),
(28, 'Christina Daniels', 27, '70072082494', 1),
(29, 'Kristen James', 28, '22395805904', 1),
(30, 'Brianna Pitts', 29, '21533989117', 1),
(31, 'Matthew Watson', 30, '09315886431', 1),
(32, 'James Robinson', 31, '45724899817', 1),
(33, 'Mr. David Lee', 32, '47618947635', 1),
(34, 'Adam Bishop', 33, '75124885598', 1),
(35, 'Joel Simpson', 34, '74031649418', 1),
(36, 'Cynthia Williams', 35, '34042928839', 1),
(37, 'Heather Craig', 36, '57476470985', 1),
(38, 'Phillip Foster', 37, '81905247918', 1),
(39, 'Margaret Lewis', 38, '32370059029', 1),
(40, 'Julie Griffin', 39, '87044628723', 1),
(41, 'Michele Johnson', 40, '51396336250', 1),
(42, 'Lisa Bartlett', 41, '75370677624', 1),
(43, 'Alexander Harris', 42, '93605172963', 1),
(44, 'Jane Anderson', 43, '20319438264', 1),
(45, 'Gary Brown', 44, '13022686653', 1),
(46, 'Tina Garcia', 45, '43266548345', 1),
(47, 'Deanna Marks', 46, '02050926231', 1),
(48, 'Tammy Kennedy', 47, '09852688013', 1),
(49, 'David Bishop', 48, '73214766355', 1),
(50, 'Cindy Parrish', 49, '44582974577', 1),
(51, 'Neil Jackson', 0, '88123596755', 1),
(52, 'Phillip Sanchez', 1, '72905462277', 1),
(53, 'Dean Bridges', 2, '65439236932', 1),
(54, 'Rebecca Johnson', 3, '74806685745', 1),
(55, 'Jeremy Pineda', 4, '46137127498', 1),
(56, 'Brett Rodriguez', 5, '53491332302', 1),
(57, 'James Hart', 6, '18967877421', 1),
(58, 'Tracy Jones', 7, '90521462965', 1),
(59, 'Michelle Lewis', 8, '10767235447', 1),
(60, 'Daniel Nguyen MD', 9, '94419369277', 1),
(61, 'Jennifer Wilson', 10, '95540705345', 1),
(62, 'Brian Johnson', 11, '54483427400', 1),
(63, 'Jacqueline Nelson', 12, '67065781643', 1),
(64, 'Donald Booth', 13, '27979195636', 1),
(65, 'Heidi Medina', 14, '67548628389', 1),
(66, 'John Raymond', 15, '69934377464', 1),
(67, 'Mark Cox', 16, '65533113964', 1),
(68, 'Jessica James', 17, '55379950588', 1),
(69, 'Walter Stone', 18, '66404698580', 1),
(70, 'Edward Greene', 19, '37871648086', 1),
(71, 'Luke Collier', 20, '69580249812', 1),
(72, 'Carlos Burns', 21, '21873366437', 1),
(73, 'Daniel Woods', 22, '83928649419', 1),
(74, 'Anthony Cruz', 23, '43744267943', 1),
(75, 'Michael Lin', 24, '03611805361', 1),
(76, 'Christine Cummings', 25, '57778084164', 1),
(77, 'Thomas Graves', 26, '77638979694', 1),
(78, 'Dr. Julie Bender', 27, '67059853967', 1),
(79, 'Corey Stone', 28, '34101185315', 1),
(80, 'Lee Harmon', 29, '37663677550', 1),
(81, 'John Hopkins', 30, '94384905629', 1),
(82, 'Stephanie Nelson', 31, '89531674487', 1),
(83, 'Patricia Wall', 32, '96580593434', 1),
(84, 'Hannah Tucker', 33, '39230732291', 1),
(85, 'Anthony Dillon', 34, '04842325016', 1),
(86, 'Kaitlyn Villarreal', 35, '35886856123', 1),
(87, 'Brad Clark', 36, '34542774330', 1),
(88, 'Kelly Carroll', 37, '51885015081', 1),
(89, 'James Perez', 38, '40329386233', 1),
(90, 'Amy Bryant', 39, '94918650588', 1),
(91, 'Kelsey Goodwin', 40, '84295316421', 1),
(92, 'Victoria Harris', 41, '87274566368', 1),
(93, 'Curtis Clark', 42, '48058438256', 1),
(94, 'Todd Day', 43, '70260876474', 1),
(95, 'Douglas Carter', 44, '13595852248', 1),
(96, 'Joel Wood', 45, '17548933300', 1),
(97, 'Mary Baker', 46, '36394061192', 1),
(98, 'Sheila Miller', 47, '26566031591', 1),
(99, 'Michael Baker', 48, '05926334566', 1),
(100, 'Lisa Torres', 49, '16549152326', 1),
(101, 'Peter Martinez', 0, '96565500833', 1),
(102, 'Stacey Thompson', 1, '71841239400', 1),
(103, 'Eric Hughes', 2, '98118749962', 1),
(104, 'Traci Clayton', 3, '22415007218', 1),
(105, 'Krista Gonzales', 4, '08742310081', 1),
(106, 'Pamela Collins', 5, '18077446219', 1),
(107, 'George Callahan', 6, '96020281214', 1),
(108, 'Jamie Fletcher', 7, '35533448636', 1),
(109, 'Deborah Ferrell', 8, '89265891728', 1),
(110, 'Tina Thomas', 9, '65634043130', 1),
(111, 'Carolyn Rivera', 10, '19497449359', 1),
(112, 'Stephen Evans', 11, '00203729585', 1),
(113, 'Brian Jones', 12, '58594027017', 1),
(114, 'Christopher Thomas', 13, '15717638292', 1),
(115, 'Philip Greer', 14, '71845250541', 1),
(116, 'James Martin', 15, '02374335059', 1),
(117, 'Jacob Reeves', 16, '80135241812', 1),
(118, 'Dennis Williams', 17, '08216803744', 1),
(119, 'Joanna Fox', 18, '66616244118', 1),
(120, 'Amanda Knight', 19, '37784330757', 1),
(121, 'Jill Jackson', 20, '58091314755', 1),
(122, 'Brianna Brown', 21, '43734340182', 1),
(123, 'Aaron Baker', 22, '41830722377', 1),
(124, 'Sarah Dennis', 23, '40783656978', 1),
(125, 'Monica Miller', 24, '43823105991', 1),
(126, 'John Moore', 25, '07852978474', 1),
(127, 'Lori Fitzpatrick', 26, '30253624520', 1),
(128, 'Ashley Edwards', 27, '58029610588', 1),
(129, 'Craig Lawson', 28, '18387361904', 1),
(130, 'Evelyn Mcdaniel', 29, '14740168955', 1),
(131, 'Vicki Rhodes', 30, '13572999629', 1),
(132, 'Bruce Lee', 31, '50054501100', 1),
(133, 'David Nelson', 32, '39363200014', 1),
(134, 'Alexander George', 33, '71194083933', 1),
(135, 'Dr. Joseph Charles', 34, '19519000003', 1),
(136, 'Mrs. Michelle Schmitt', 35, '96302465129', 1),
(137, 'Adam Sexton Jr.', 36, '92862435658', 1),
(138, 'John Mercer', 37, '22723904367', 1),
(139, 'Tamara Mccormick', 38, '13116021093', 1),
(140, 'Deborah Rowe', 39, '73648323885', 1),
(141, 'Meghan Williams', 40, '46636600423', 1),
(142, 'Brandi Murphy', 41, '08251113161', 1),
(143, 'Kimberly Smith', 42, '25666437785', 1),
(144, 'Joshua Cameron', 43, '05081389862', 1),
(145, 'Melissa Farley', 44, '54483096378', 1),
(146, 'Andrew Reed', 45, '60373003402', 1),
(147, 'Eric Griffith', 46, '45370478961', 1),
(148, 'Luis Rich', 47, '54222532040', 1),
(149, 'Brittany Campos', 48, '29601151352', 1),
(150, 'Justin Johnson', 49, '77554569662', 1);

-- --------------------------------------------------------

--
-- Table structure for table `pdf`
--

DROP TABLE IF EXISTS `pdf`;
CREATE TABLE IF NOT EXISTS `pdf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `src` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
CREATE TABLE IF NOT EXISTS `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `src` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `private_message`
--

DROP TABLE IF EXISTS `private_message`;
CREATE TABLE IF NOT EXISTS `private_message` (
  `locking_preiod` int(11) DEFAULT NULL,
  `text` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `seen` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `question_bank`
--

DROP TABLE IF EXISTS `question_bank`;
CREATE TABLE IF NOT EXISTS `question_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  `Teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Teacher_id` (`Teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `question_details`
--

DROP TABLE IF EXISTS `question_details`;
CREATE TABLE IF NOT EXISTS `question_details` (
  `type_with_content` json DEFAULT NULL,
  `Question_store_id` int(11) DEFAULT NULL,
  KEY `Question_store_id` (`Question_store_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question_details`
--

INSERT INTO `question_details` (`type_with_content`, `Question_store_id`) VALUES
('{\"type\": \"true_false\", \"question\": {\"q1\": \"true\", \"q2\": \"false\", \"q3\": \"true\"}}', 55),
('{\"type\": \"true_false\", \"question\": {\"q1\": \"true\", \"q2\": \"false\", \"q3\": \"true\"}}', 55),
('{\"type\": 2, \"question\": {\"q2\": \"false\", \"q3\": \"shit again\", \"shit\": \"true\"}}', 200),
('{\"type\": 2, \"question\": {\"q2\": \"false\", \"q3\": \"shit again\", \"shit\": \"true\"}}', 0),
('{\"type\": 2, \"question\": {\"q2\": \"false\", \"q3\": \"shit again\", \"shit\": \"true\"}}', 1),
('{\"type\": 2, \"question\": {\"q2\": \"false\", \"q3\": \"shit again\", \"shit\": \"true\"}}', 2),
('{\"type\": 2, \"question\": {\"q2\": \"false\", \"q3\": \"shit again\", \"shit\": \"true\"}}', 3);

-- --------------------------------------------------------

--
-- Table structure for table `question_store`
--

DROP TABLE IF EXISTS `question_store`;
CREATE TABLE IF NOT EXISTS `question_store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  `bank_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`),
  KEY `bank_id` (`bank_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `question_submission`
--

DROP TABLE IF EXISTS `question_submission`;
CREATE TABLE IF NOT EXISTS `question_submission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_answer` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  `Question_store_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Question_store_id` (`Question_store_id`),
  KEY `student_id` (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `time` varchar(11) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`id`, `name`, `time`, `lesson_id`, `teacher_id`) VALUES
(52, 'shit', '0', 1, 154),
(54, 'e', '17:04', 1, 152),
(50, 'sa fuck you', '16:39', 1, 0),
(42, 'rrrrrrrrrrrrr', '23:18', 1, 0),
(43, 'a', '23:38', 1, 0),
(46, 'hi2', '03:25', 1, 0),
(47, 'ww', '03:31', 1, 0),
(48, 'dafuck', '03:32', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(120) NOT NULL,
  `school` varchar(50) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  `center_online` tinyint(1) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`)
) ENGINE=MyISAM AUTO_INCREMENT=152 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `full_name`, `username`, `email`, `password`, `school`, `phone`, `stage`, `center_online`, `img`, `parent_id`) VALUES
(151, 'TAKnight101', 'TAKnight101', 'yagamiLayto1988@gmail.com', 'pbkdf2:sha256:150000$VlRATGMZ$197c6eede95678da8e8e0a737943ae98cd62d346caf0ed164f4bfcd155991aec', 'el salam', '0101212321', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `student_result`
--

DROP TABLE IF EXISTS `student_result`;
CREATE TABLE IF NOT EXISTS `student_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  `precentage` int(11) DEFAULT NULL,
  `outof` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  KEY `exam_id` (`exam_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
CREATE TABLE IF NOT EXISTS `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=156 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `full_name`, `email`, `phone`, `stage`, `img`) VALUES
(155, 'Michael Davis', 'jsaunders@andrews.com', '57507342087', 1, NULL),
(154, 'Emily Logan', 'davidjohnson@yahoo.com', '26158037426', 1, NULL),
(153, 'Margaret Ray', 'chrisrodriguez@johnston.com', '52099717037', 1, NULL),
(152, 'Jeffrey Avery', 'mhernandez@hotmail.com', '65550028473', 1, NULL),
(151, 'Brian Benson', 'simmonsthomas@gmail.com', '74902256355', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
CREATE TABLE IF NOT EXISTS `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `src` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `video_interactive`
--

DROP TABLE IF EXISTS `video_interactive`;
CREATE TABLE IF NOT EXISTS `video_interactive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `instant_number` int(11) DEFAULT NULL,
  `time_instant` int(11) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
